from django.shortcuts import render, redirect

from my_plant_app.plant_app.forms import PlantCreateForm, PlantEditForm, PlantDeleteForm
from my_plant_app.plant_app.models import Plant


# Create your views here.
def create_plant(request):
    form = PlantCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'plant/create-plant.html', context)


def details_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    context = {
        'plant': plant
    }
    return render(request, 'plant/plant-details.html', context)


def edit_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    form = PlantEditForm(request.POST or None, instance=plant)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant
    }
    return render(request, 'plant/edit-plant.html', context)


def delete_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    form = PlantDeleteForm(request.POST or None, instance=plant)
    if form.is_valid():
        plant.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant
    }
    return render(request, 'plant/delete-plant.html', context)
