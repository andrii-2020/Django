from django.shortcuts import render

from .models import Owner, Animals
from time import gmtime, strftime
# Create your views here.


def home(request):
    # %Y - %m - %d %H:%M:%S
    t = strftime("%m-%d-%Y", gmtime())
    return render(request, 'homee.html', {'t': t})


def owner(request):
    qs = Owner.objects.all()
    qs = qs.order_by('name')
    return render(request, 'owner.html', {'owner': qs})


def animals(request):
    qs1 = Animals.objects.all()
    qs1 = qs1.order_by('name')
    return render(request, 'animals.html', {'animals': qs1})


def cal(request, calc, string, cal):
    if string == 'add':
        res = calc.__add__(cal)
        string = '+'
    elif string == 'sub':
        string = '-'
        res = calc.__sub__(cal)
    elif string == 'mul':
        string = '*'
        res = calc.__mul__(cal)

    return render(request, 'calcu.html', {'res': res, 'calc': calc, 'cal': cal, 'str': string})


