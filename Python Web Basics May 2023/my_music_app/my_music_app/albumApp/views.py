from django.shortcuts import render, redirect

from my_music_app.albumApp.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from my_music_app.albumApp.models import Album


# Create your views here.
def add_album(request):
    form = AlbumCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'album/add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album
    }
    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    form = AlbumEditForm(request.POST or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'album': album
    }
    return render(request, 'album/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    form = AlbumDeleteForm(request.POST or None, instance=album)
    if form.is_valid():
        album.delete()
        return redirect('index')

    context = {
        'form': form,
        'album': album
    }

    return render(request, 'album/delete-album.html', context)

