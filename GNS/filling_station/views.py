from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Ballon
from .forms import Process, OperatorControl
from datetime import datetime
import locale



locale.setlocale(locale.LC_TIME, "ru-RU")


def index(request):
    ballons = Ballon.objects.all()
    return render(request, "home.html", {"ballons": ballons})


def client(request):
    ballons = Ballon.objects.all()
    return render(request, "home.html", {"ballons": ballons})


def operator(request):
    ballons = Ballon.objects.order_by('-creation_date')
    paginator = Paginator(ballons, 5)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, "ballons_table.html", {"page_obj": page_obj})
