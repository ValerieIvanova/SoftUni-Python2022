from django.shortcuts import render

from fruitipedia.fruitApp.models import Fruit


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()
    context = {
        'fruits': fruits.order_by('pk')
    }
    return render(request, 'common/dashboard.html', context)