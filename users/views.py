from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def logout_view(request):
    """Завершает сеанс работы с приложением"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """Регистрация нового пользователя"""
    if request.method != 'POST':
        # Выводит поле регистрации пользователя
        form = UserCreationForm()
    else:
        # Обработка заполненных форм
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
