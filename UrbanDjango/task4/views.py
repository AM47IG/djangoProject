from django.shortcuts import render


# Create your views here.
def games(request):
    games = {'games': ["Atomic Heart 3", "Cyberpunk 2088", 'PayDay 4']}
    return render(request, 'fourth_task/games.html', context={'games': games})
