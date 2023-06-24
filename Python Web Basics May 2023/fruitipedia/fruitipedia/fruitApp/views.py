from django.shortcuts import render, redirect

from fruitipedia.fruitApp.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from fruitipedia.fruitApp.models import Fruit


# Create your views here.
def create_fruit(request):
    form = FruitCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'fruit/create-fruit.html', context)


def details_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    context = {
        'fruit': fruit
    }
    return render(request, 'fruit/details-fruit.html', context)


def edit_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = FruitEditForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form
    }
    return render(request, 'fruit/edit-fruit.html', context)


def delete_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = FruitDeleteForm(request.POST or None, instance=fruit)
    if form.is_valid():
        fruit.delete()
        return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form
    }

    return render(request, 'fruit/delete-fruit.html', context)