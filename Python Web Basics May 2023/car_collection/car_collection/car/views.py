from django.shortcuts import render, redirect
from .forms import CarCreateForm, CarEditForm, CarDeleteForm
from .models import Car


# Create your views here.

def car_create(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }
    return render(request, 'car/car-create.html', context)


def car_edit(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    # Another way to do this without if statements:

    # form = CarEditForm(request.POST or None, instance=car)
    # if form.is_valid():
    #     form.save()
    #     return redirect('catalogue')

    context = {
        'form': form,
        'car': car
    }
    return render(request, 'car/car-edit.html', context)


def car_details(request, pk):
    car = Car.objects.get(pk=pk)
    context = {
        'car': car
    }

    return render(request, 'car/car-details.html', context)


def car_delete(request, pk):
    car = Car.objects.get(pk=pk)
    form = CarDeleteForm(request.POST or None, instance=car)
    if form.is_valid():
        car.delete()
        return redirect('catalogue')

    context = {
        'car': car,
        'form': form
    }

    return render(request, 'car/car-delete.html', context)
