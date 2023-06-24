from django.db.models import Avg
from django.shortcuts import render, redirect

from gamesPlay.gameApp.models import Game
from gamesPlay.profileApp.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from gamesPlay.profileApp.models import Profile


# Create your views here.
def create_profile(request):
    form = ProfileCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home-page')

    context = {
        'form': form
    }
    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    games = Game.objects.all()
    games_count = games.count() if games else 0
    average_rating = games.aggregate(Avg('rating'))['rating__avg']
    if average_rating is None:
        average_rating = 0.0

    context = {
        'average_rating': average_rating,
        'games_count': games_count
    }
    return render(request, 'profile/details-profile.html', context)


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


def delete_profile(request):
    user = Profile.objects.first()
    if request.method == 'POST':
        user.delete()
        Game.objects.all().delete()
        return redirect('home-page')

    return render(request, 'profile/delete-profile.html')