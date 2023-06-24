from django.shortcuts import render, redirect

from .forms import ProfileCreateForm, ProfileEditForm
from .models import Profile
from ..car.models import Car


# Create your views here.


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    user = Profile.objects.get()
    cars = Car.objects.all()
    total_price = sum(car.price for car in cars)

    context = {
        'user': user,
        'total_price': total_price
    }

    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    user = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileEditForm(instance=user)
    else:
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile-details')

    context = {
        'form': form
    }
    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    if request.method == 'POST':
        Car.objects.all().delete()
        Profile.objects.first().delete()
        return redirect('index')

    return render(request, 'profile/profile-delete.html')
