from django.shortcuts import render, redirect

from my_music_app.albumApp.models import Album
from my_music_app.profileApp.models import Profile


# Create your views here.
def delete_profile(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()
    if request.method == 'POST':
        profile.delete()
        albums.delete()
        return redirect('index')

    context = {
        'profile': profile,
    }
    return render(request, 'profile/profile-delete.html', context)


def details_profile(request):
    albums_count = Album.objects.all().count()
    context = {
        'albums_count': albums_count
    }
    return render(request, 'profile/profile-details.html', context)
