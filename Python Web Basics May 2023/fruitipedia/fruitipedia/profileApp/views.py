from django.shortcuts import render, redirect

from fruitipedia.fruitApp.models import Fruit
from fruitipedia.profileApp.forms import ProfileCreateForm, ProfileEditForm
from fruitipedia.profileApp.models import Profile


# Create your views here.
def create_profile(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    posts_count = Fruit.objects.all().count()
    context = {
        'posts_count': posts_count
    }
    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    user = Profile.objects.first()
    form = ProfileEditForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('details_profile')

    context = {
        'form': form
    }
    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        Fruit.objects.all().delete()
        profile.delete()
        return redirect('index')

    return render(request, 'profile/delete-profile.html')

