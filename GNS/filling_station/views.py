from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q
from .models import (Balloon, Truck, Trailer, TTN, BalloonsLoadingBatch, BalloonsUnloadingBatch,
                     BalloonAmount, AutoGasBatch, Reader, Carousel)
from .admin import BalloonResources
from .forms import (GetBalloonsAmount, BalloonForm, TruckForm, TrailerForm, TTNForm,
                    BalloonsLoadingBatchForm, BalloonsUnloadingBatchForm, AutoGasBatchForm)
from datetime import datetime, timedelta

STATUS_LIST = {
    1: 'Погрузка полного баллона на трал 1',
    2: 'Погрузка полного баллона на трал 2',
    3: 'Приёмка пустого баллона из трала 1',
    4: 'Приёмка пустого баллона из трала 2',
    5: 'Регистрация полного баллона на складе',
    6: 'Регистрация пустого баллона в цеху',
    7: 'Наполнение баллона сжиженным газом. Карусель №1',
    8: 'Наполнение баллона сжиженным газом. Карусель №2',
    9: 'Вход в наполнительный цех из ремонтного',
    10: 'Выход из наполнительного цеха в ремонтный',
    11: 'Вход в ремонтный цех из наполнительного',
    12: 'Выход из ремонтного цеха в наполнительный',
}


class BalloonListView(generic.ListView):
    model = Balloon
    paginate_by = 15

    def get_queryset(self):
        query = self.request.GET.get('query', '')

        if query:
            return Balloon.objects.filter(
                Q(nfc_tag=query) | Q(serial_number=query)
            )
        else:
            return Balloon.objects.all()


class BalloonDetailView(generic.DetailView):
    model = Balloon


class BalloonUpdateView(generic.UpdateView):
    model = Balloon
    form_class = BalloonForm
    template_name = 'filling_station/_equipment_form.html'


class BalloonDeleteView(generic.DeleteView):
    model = Balloon
    success_url = reverse_lazy("filling_station:balloon_list")
    template_name = 'filling_station/balloon_confirm_delete.html'


def reader_info(request, reader=1):
    current_date = datetime.now().date()
    previous_date = current_date - timedelta(days=1)

    if request.method == "POST":
        required_date = request.POST.get("date")
        format_required_date = datetime.strptime(required_date, '%Y-%m-%d')

        # Экспортируем данные в Excel
        dataset = BalloonResources().export(Reader.objects.filter(number=reader, change_date=format_required_date))
        response = HttpResponse(dataset.xlsx, content_type='xlsx')
        response['Content-Disposition'] = f'attachment; filename="RFID_{reader}_{required_date}.xlsx"'

        return response
    else:
        date_process = GetBalloonsAmount()

    balloons_list = Reader.objects.order_by('-change_date', '-change_time').filter(number=reader)
    current_quantity = BalloonAmount.objects.filter(reader_id=reader, change_date=current_date).first()
    previous_quantity = BalloonAmount.objects.filter(reader_id=reader, change_date=previous_date).first()

    if current_quantity is not None:
        current_quantity_rfid = current_quantity.amount_of_rfid
        current_quantity_balloons = current_quantity.amount_of_balloons
    else:
        current_quantity_rfid = 0
        current_quantity_balloons = 0

    if previous_quantity is not None:
        previous_quantity_rfid = previous_quantity.amount_of_rfid
        previous_quantity_balloons = previous_quantity.amount_of_balloons
    else:
        previous_quantity_rfid = 0
        previous_quantity_balloons = 0

    paginator = Paginator(balloons_list, 15)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    context = {
        "page_obj": page_obj,
        'current_quantity_by_reader': current_quantity_rfid,
        'previous_quantity_by_reader': previous_quantity_rfid,
        'current_quantity_by_sensor': current_quantity_balloons,
        'previous_quantity_by_sensor': previous_quantity_balloons,
        'form': date_process,
        'reader': reader,
        'reader_status': STATUS_LIST[reader]
    }
    return render(request, "rfid_tables.html", context)


class CarouselListView(generic.ListView):
    model = Carousel
    paginate_by = 15
    template_name = 'filling_station/carousel_list.html'


# Партии приёмки баллонов
class BalloonLoadingBatchListView(generic.ListView):
    model = BalloonsLoadingBatch
    paginate_by = 15
    template_name = 'filling_station/balloon_batch_list.html'


class BalloonLoadingBatchDetailView(generic.DetailView):
    model = BalloonsLoadingBatch
    context_object_name = 'batch'
    template_name = 'filling_station/balloon_batch_detail.html'


class BalloonLoadingBatchUpdateView(generic.UpdateView):
    model = BalloonsLoadingBatch
    form_class = BalloonsLoadingBatchForm
    template_name = 'filling_station/_equipment_form.html'


class BalloonLoadingBatchDeleteView(generic.DeleteView):
    model = BalloonsLoadingBatch
    success_url = reverse_lazy("filling_station:balloon_loading_batch_list")
    template_name = 'filling_station/balloons_loading_batch_confirm_delete.html'


# Партии отгрузки баллонов
class BalloonUnloadingBatchListView(generic.ListView):
    model = BalloonsUnloadingBatch
    paginate_by = 15
    template_name = 'filling_station/balloon_batch_list.html'


class BalloonUnloadingBatchDetailView(generic.DetailView):
    model = BalloonsUnloadingBatch
    context_object_name = 'batch'
    template_name = 'filling_station/balloon_batch_detail.html'


class BalloonUnloadingBatchUpdateView(generic.UpdateView):
    model = BalloonsUnloadingBatch
    form_class = BalloonsUnloadingBatchForm
    template_name = 'filling_station/_equipment_form.html'


class BalloonUnloadingBatchDeleteView(generic.DeleteView):
    model = BalloonsUnloadingBatch
    success_url = reverse_lazy("filling_station:balloon_unloading_batch_list")
    template_name = 'filling_station/balloons_unloading_batch_confirm_delete.html'


# Партии автоцистерн
class AutoGasBatchListView(generic.ListView):
    model = AutoGasBatch
    paginate_by = 15
    template_name = 'filling_station/auto_batch_list.html'


class AutoGasBatchDetailView(generic.DetailView):
    model = AutoGasBatch
    context_object_name = 'batch'
    template_name = 'filling_station/auto_batch_detail.html'


class AutoGasBatchUpdateView(generic.UpdateView):
    model = AutoGasBatch
    form_class = AutoGasBatchForm
    template_name = 'filling_station/_equipment_form.html'


class AutoGasBatchDeleteView(generic.DeleteView):
    model = AutoGasBatch
    success_url = reverse_lazy("filling_station:auto_gas_batch_list")
    template_name = 'filling_station/auto_batch_confirm_delete.html'


# Грузовики
class TruckView(generic.ListView):
    model = Truck
    paginate_by = 15


class TruckDetailView(generic.DetailView):
    model = Truck


class TruckCreateView(generic.CreateView):
    model = Truck
    form_class = TruckForm
    template_name = 'filling_station/_equipment_form.html'
    success_url = reverse_lazy("filling_station:truck_list")


class TruckUpdateView(generic.UpdateView):
    model = Truck
    form_class = TruckForm
    template_name = 'filling_station/_equipment_form.html'


class TruckDeleteView(generic.DeleteView):
    model = Truck
    success_url = reverse_lazy("filling_station:truck_list")
    template_name = 'filling_station/truck_confirm_delete.html'


# Прицепы
class TrailerView(generic.ListView):
    model = Trailer
    paginate_by = 15


class TrailerDetailView(generic.DetailView):
    model = Trailer

    
class TrailerCreateView(generic.CreateView):
    model = Trailer
    form_class = TrailerForm
    template_name = 'filling_station/_equipment_form.html'
    success_url = reverse_lazy("filling_station:trailer_list")


class TrailerUpdateView(generic.UpdateView):
    model = Trailer
    form_class = TrailerForm
    template_name = 'filling_station/_equipment_form.html'


class TrailerDeleteView(generic.DeleteView):
    model = Trailer
    success_url = reverse_lazy("filling_station:trailer_list")
    template_name = 'filling_station/trailer_confirm_delete.html'


# ТТН
class TTNView(generic.ListView):
    model = TTN
    paginate_by = 15


class TTNDetailView(generic.DetailView):
    model = TTN

    
class TTNCreateView(generic.CreateView):
    model = TTN
    form_class = TTNForm
    template_name = 'filling_station/_equipment_form.html'
    success_url = reverse_lazy("filling_station:ttn_list")


class TTNUpdateView(generic.UpdateView):
    model = TTN
    form_class = TTNForm
    template_name = 'filling_station/_equipment_form.html'


class TTNDeleteView(generic.DeleteView):
    model = TTN
    success_url = reverse_lazy("filling_station:ttn_list")
    template_name = 'filling_station/ttn_confirm_delete.html'
