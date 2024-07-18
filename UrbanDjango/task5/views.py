from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def sign_up_by_html(request):
    users = ['Иван', 'Мария']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username') not in users
        password = request.POST.get('password') == request.POST.get('repeat_password')
        age = int(request.POST.get('age')) >= 18
        if username and password and age:
            return HttpResponse(f'Приветствуем, {request.POST.get('username')}!')
        if not username:
            info['error'] = 'Пользователь уже существует'
        elif not password:
            info['error'] = 'Пароли не совпадают'
        elif not age:
            info['error'] = 'Вы должны быть старше 18'
    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_django(request):
    users = ['Иван', 'Мария']
    form = UserRegister()
    info = {'form': form}
    if request.method == 'POST':
        form = UserRegister(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') not in users
            password = form.cleaned_data.get('password') == form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age') >= 18
            if username and password and age:
                return HttpResponse(f'Приветствуем, {form.cleaned_data.get('username')}!')
            if not username:
                info['error'] = 'Пользователь уже существует'
            elif not password:
                info['error'] = 'Пароли не совпадают'
            elif not age:
                info['error'] = 'Вы должны быть старше 18'
    return render(request, 'fifth_task/registration_page.html', context=info)
