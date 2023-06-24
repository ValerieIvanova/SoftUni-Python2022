from django.shortcuts import render
from ..car.models import Car


# Create your views here.

def index(request):
    return render(request, 'common/index.html')


def catalogue(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'common/catalogue.html', context)
