from django.shortcuts import render
from ..plant_app.models import Plant


# Create your views here.


def home_page(request):
    return render(request, 'common/home-page.html')


def catalogue(request):
    plants = Plant.objects.all()
    context = {
        'plants': plants.order_by('pk')
    }
    return render(request, 'common/catalogue.html', context)
