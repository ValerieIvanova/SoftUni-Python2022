from django.shortcuts import render, redirect

from .models import Profile
from ..plant_app.models import Plant
from ..profile_app.forms import ProfileCreateForm, ProfileEditForm


# Create your views here.

def create_profile(request):
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
    return render(request, 'profile/create-profile.html', context)


def delete_profile(request):
    user = Profile.objects.first()
    if request.method == 'POST':
        user.delete()
        Plant.objects.all().delete()
        return redirect('home-page')

    return render(request, 'profile/delete-profile.html')


def edit_profile(request):
    user = Profile.objects.first()
    form = ProfileEditForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('details-profile')

    context = {
        'form': form
    }

    return render(request, 'profile/edit-profile.html', context)


def details_profile(request):
    plants = Plant.objects.all()
    context = {
        'plants': plants
    }
    return render(request, 'profile/profile-details.html', context)
