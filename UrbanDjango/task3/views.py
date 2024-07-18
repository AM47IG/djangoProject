from django.shortcuts import render


# Create your views here.
def games(request):
    games = ['Atomic Heart 2', 'Cyberpunk 2088', 'PayDay 4']
    return render(request, 'third_task/games.html', context={'games': games})
