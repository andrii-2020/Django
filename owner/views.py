from django.shortcuts import render

from .models import Owner, Animals
from time import gmtime, strftime
# Create your views here.
from .forms import OwnerForm, AnimalForm


def home(request):
    # %Y - %m - %d %H:%M:%S
    t = strftime("%m - %d - %Y", gmtime())
    return render(request, 'homee.html', {'t': t})


def owners(request):
    qs = Owner.objects.all()
    form = OwnerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, 'owner.html', {'owner': qs, 'form': form})


def animals(request):
    qs1 = Animals.objects.all()
    formA = AnimalForm(request.POST)
    if request.method == 'POST':
        if formA.is_valid():
            formA.save()
    return render(request, 'animals.html', {'animals': qs1, 'formA': formA})


def owner(request, id):
    try:
        o = Owner.objects.get(pk=id).animal.all()
    except Exception:
        o = None
    return render(request, 'owne-animal.html', {'animals': o})