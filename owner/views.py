from django.shortcuts import render

from .models import Owner, Animals
# Create your views here.


def home(request):
    return render(request, 'homee.html')


def owner(request):
    qs = Owner.objects.all()
    #id = Owner.objects.get(id=3)
    return render(request, 'owner.html', {'owner': qs})


def animals(request):
    qs1 = Animals.objects.all()
    return render(request, 'animals.html', {'animals': qs1})