from django.shortcuts import render, redirect

from gamesPlay.gameApp.forms import GameCreateForm, GameEditForm, GameDeleteForm
from gamesPlay.gameApp.models import Game


# Create your views here.
def create_game(request):
    form = GameCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'game/create-game.html', context)


def details_game(request, pk):
    game = Game.objects.get(id=pk)
    context = {
        'game': game
    }
    return render(request, 'game/details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.get(id=pk)
    form = GameEditForm(request.POST or None, instance=game)

    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form,
        'game': game
    }
    return render(request, 'game/edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.get(pk=pk)
    form = GameDeleteForm(request.POST or None, instance=game)
    if form.is_valid():
        game.delete()
        return redirect('dashboard')

    context = {
        'form': form,
        'game': game
    }
    return render(request, 'game/delete-game.html', context)
