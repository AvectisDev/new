from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ballon
from .forms import Process, OperatorControl
from datetime import datetime
import locale



locale.setlocale(locale.LC_TIME, "ru-RU")


def index(request):
    ballons = Ballon.objects.all()
    return render(request, "home.html", {"ballons": ballons})
