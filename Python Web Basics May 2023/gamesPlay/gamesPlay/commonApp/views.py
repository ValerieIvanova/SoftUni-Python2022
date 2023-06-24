from django.shortcuts import render

from gamesPlay.gameApp.models import Game


# Create your views here.
def home_page(request):
    return render(request, 'common/home-page.html')


def dashboard(request):
    games = Game.objects.all()
    context = {
        'games': games.order_by('pk')
    }

    return render(request, 'common/dashboard.html', context)
