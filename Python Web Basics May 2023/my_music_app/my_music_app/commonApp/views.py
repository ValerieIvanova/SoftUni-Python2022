from django.shortcuts import render, redirect

from my_music_app.albumApp.models import Album
from my_music_app.commonApp.forms import ProfileCreateForm
from my_music_app.commonApp.templatetags.get_profile import get_user_profile


# Create your views here.
def index(request):
    profile = get_user_profile()
    if not profile:
        form = ProfileCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'profile': profile,
            'form': form
        }
        return render(request, 'common/home-no-profile.html', context)
    else:
        albums = Album.objects.all()
        context = {
            'profile': profile,
            'albums': albums.order_by('pk')
        }
        return render(request, 'common/home-with-profile.html', context)


