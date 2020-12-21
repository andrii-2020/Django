from django.shortcuts import render

from .models import Owner, Animals
from time import gmtime, strftime
# Create your views here.


def home(request):
    # %Y - %m - %d %H:%M:%S
    t = strftime("%m - %d - %Y", gmtime())
    return render(request, 'homee.html', {'t': t})


def owner(request):
    qs = Owner.objects.all()
    return render(request, 'owner.html', {'owner': qs})


def animals(request):
    qs1 = Animals.objects.all()
    return render(request, 'animals.html', {'animals': qs1})