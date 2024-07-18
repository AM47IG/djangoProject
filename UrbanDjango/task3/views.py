from django.shortcuts import render


# Create your views here.
def games(request):
    games = {'first': "Atomic Heart 3", 'second': "Cyberpunk 2088", 'third': 'PayDay 4'}
    return render(request, 'third_task/games.html', context={'games': games})
