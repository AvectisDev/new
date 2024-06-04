from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Ballon
from .forms import Process, GetBallonsAmount
from datetime import datetime, date, time, timedelta
import locale



# locale.setlocale(locale.LC_TIME, "ru-RU")


def index(request):
    ballons = Ballon.objects.all()
    return render(request, "home.html", {"ballons": ballons})


def client(request):
    ballons = Ballon.objects.all()
    return render(request, "home.html", {"ballons": ballons})


def reader1(request):
    ballons = Ballon.objects.order_by('-id').filter(state = 'Регистрация пустого баллона на складе (цех)')
    paginator = Paginator(ballons, 15)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    format = '%d.%m.%Y'

    date_process = GetBallonsAmount()
    if request.method == "POST":
        required_date = request.POST.get("date")
        format_required_date = datetime.strptime(required_date, format)
    else:
        date_process = GetBallonsAmount()
        format_required_date = datetime.today()

    last_date_amount = len(ballons.filter(creation_date = datetime.today()))
    previous_date_amount = len(ballons.filter(creation_date = datetime.today() - timedelta(days=1)))     
    required_date_amount = len(ballons.filter(creation_date = format_required_date))

    view_required_data = datetime.strftime(format_required_date, format)
    return render(request, "ballons_table_1.html", {
        "page_obj": page_obj, 
        'ballons_amount': last_date_amount, 
        'previous_ballons_amount': previous_date_amount,
        'required_date_amount': required_date_amount,
        'format_required_date': view_required_data,
        'form': date_process})

def reader2(request):
    ballons = Ballon.objects.order_by('-id').filter(state = 'Наполнение баллона сжиженным газом')
    paginator = Paginator(ballons, 15)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    format = '%d.%m.%Y'

    date_process = GetBallonsAmount()
    if request.method == "POST":
        required_date = request.POST.get("date")
        format_required_date = datetime.strptime(required_date, format)
    else:
        date_process = GetBallonsAmount()
        format_required_date = datetime.today()

    last_date_amount = len(ballons.filter(creation_date = datetime.today()))
    previous_date_amount = len(ballons.filter(creation_date = datetime.today() - timedelta(days=1)))     
    required_date_amount = len(ballons.filter(creation_date = format_required_date))

    view_required_data = datetime.strftime(format_required_date, format)
    return render(request, "ballons_table_2.html", {
        "page_obj": page_obj, 
        'ballons_amount': last_date_amount, 
        'previous_ballons_amount': previous_date_amount,
        'required_date_amount': required_date_amount,
        'format_required_date': view_required_data,
        'form': date_process})

def reader3(request):
    ballons = Ballon.objects.order_by('-id').filter(state = 'Регистрация пустого баллона на складе (рампа)')
    paginator = Paginator(ballons, 15)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    format = '%d.%m.%Y'

    date_process = GetBallonsAmount()
    if request.method == "POST":
        required_date = request.POST.get("date")
        format_required_date = datetime.strptime(required_date, format)
    else:
        date_process = GetBallonsAmount()
        format_required_date = datetime.today()

    last_date_amount = len(ballons.filter(creation_date = datetime.today()))
    previous_date_amount = len(ballons.filter(creation_date = datetime.today() - timedelta(days=1)))     
    required_date_amount = len(ballons.filter(creation_date = format_required_date))

    view_required_data = datetime.strftime(format_required_date, format)
    return render(request, "ballons_table_3.html", {
        "page_obj": page_obj, 
        'ballons_amount': last_date_amount, 
        'previous_ballons_amount': previous_date_amount,
        'required_date_amount': required_date_amount,
        'format_required_date': view_required_data,
        'form': date_process})

def reader4(request):
    ballons = Ballon.objects.order_by('-id').filter(state = 'Регистрация полного баллона на складе')
    paginator = Paginator(ballons, 15)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    format = '%d.%m.%Y'

    date_process = GetBallonsAmount()
    if request.method == "POST":
        required_date = request.POST.get("date")
        format_required_date = datetime.strptime(required_date, format)
    else:
        date_process = GetBallonsAmount()
        format_required_date = datetime.today()

    last_date_amount = len(ballons.filter(creation_date = datetime.today()))
    previous_date_amount = len(ballons.filter(creation_date = datetime.today() - timedelta(days=1)))     
    required_date_amount = len(ballons.filter(creation_date = format_required_date))

    view_required_data = datetime.strftime(format_required_date, format)
    return render(request, "ballons_table_4.html", {
        "page_obj": page_obj, 
        'ballons_amount': last_date_amount, 
        'previous_ballons_amount': previous_date_amount,
        'required_date_amount': required_date_amount,
        'format_required_date': view_required_data,
        'form': date_process})

def reader5(request):
    ballons = Ballon.objects.order_by('-id').filter(state = 'Погрузка полного баллона на тралл 2')
    paginator = Paginator(ballons, 15)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    format = '%d.%m.%Y'

    date_process = GetBallonsAmount()
    if request.method == "POST":
        required_date = request.POST.get("date")
        format_required_date = datetime.strptime(required_date, format)
    else:
        date_process = GetBallonsAmount()
        format_required_date = datetime.today()

    last_date_amount = len(ballons.filter(creation_date = datetime.today()))
    previous_date_amount = len(ballons.filter(creation_date = datetime.today() - timedelta(days=1)))     
    required_date_amount = len(ballons.filter(creation_date = format_required_date))

    view_required_data = datetime.strftime(format_required_date, format)
    return render(request, "ballons_table_5.html", {
        "page_obj": page_obj, 
        'ballons_amount': last_date_amount, 
        'previous_ballons_amount': previous_date_amount,
        'required_date_amount': required_date_amount,
        'format_required_date': view_required_data,
        'form': date_process})

def reader6(request):
    ballons = Ballon.objects.order_by('-id').filter(state = 'Погрузка полного баллона на тралл 1')
    paginator = Paginator(ballons, 15)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    format = '%d.%m.%Y'

    date_process = GetBallonsAmount()
    if request.method == "POST":
        required_date = request.POST.get("date")
        format_required_date = datetime.strptime(required_date, format)
    else:
        date_process = GetBallonsAmount()
        format_required_date = datetime.today()

    last_date_amount = len(ballons.filter(creation_date = datetime.today()))
    previous_date_amount = len(ballons.filter(creation_date = datetime.today() - timedelta(days=1)))     
    required_date_amount = len(ballons.filter(creation_date = format_required_date))

    view_required_data = datetime.strftime(format_required_date, format)
    return render(request, "ballons_table_6.html", {
        "page_obj": page_obj, 
        'ballons_amount': last_date_amount, 
        'previous_ballons_amount': previous_date_amount,
        'required_date_amount': required_date_amount,
        'format_required_date': view_required_data,
        'form': date_process})

def reader7(request):
    ballons = Ballon.objects.order_by('-id').filter(state = 'Погрузка полного баллона в кассету')
    paginator = Paginator(ballons, 15)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    format = '%d.%m.%Y'

    date_process = GetBallonsAmount()
    if request.method == "POST":
        required_date = request.POST.get("date")
        format_required_date = datetime.strptime(required_date, format)
    else:
        date_process = GetBallonsAmount()
        format_required_date = datetime.today()

    last_date_amount = len(ballons.filter(creation_date = datetime.today()))
    previous_date_amount = len(ballons.filter(creation_date = datetime.today() - timedelta(days=1)))     
    required_date_amount = len(ballons.filter(creation_date = format_required_date))

    view_required_data = datetime.strftime(format_required_date, format)
    return render(request, "ballons_table_7.html", {
        "page_obj": page_obj, 
        'ballons_amount': last_date_amount, 
        'previous_ballons_amount': previous_date_amount,
        'required_date_amount': required_date_amount,
        'format_required_date': view_required_data,
        'form': date_process})

def reader8(request):
    ballons = Ballon.objects.order_by('-id').filter(state = 'Регистрация пустого баллона на складе (из кассеты)')
    paginator = Paginator(ballons, 15)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    format = '%d.%m.%Y'

    date_process = GetBallonsAmount()
    if request.method == "POST":
        required_date = request.POST.get("date")
        format_required_date = datetime.strptime(required_date, format)
    else:
        date_process = GetBallonsAmount()
        format_required_date = datetime.today()

    last_date_amount = len(ballons.filter(creation_date = datetime.today()))
    previous_date_amount = len(ballons.filter(creation_date = datetime.today() - timedelta(days=1)))     
    required_date_amount = len(ballons.filter(creation_date = format_required_date))

    view_required_data = datetime.strftime(format_required_date, format)
    return render(request, "ballons_table_8.html", {
        "page_obj": page_obj, 
        'ballons_amount': last_date_amount, 
        'previous_ballons_amount': previous_date_amount,
        'required_date_amount': required_date_amount,
        'format_required_date': view_required_data,
        'form': date_process})
