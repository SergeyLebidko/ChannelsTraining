from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User

from .forms import RegisterForm


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    user = request.user
    context = {
        'data': {
            'roomName': room_name,
            'username': user.username
        }
    }
    return render(request, 'chat/room.html', context=context)


class Login(LoginView):
    template_name = 'chat/login.html'


class Logout(LogoutView):
    next_page = reverse_lazy('chat:index')


def register(request):
    context = {}
    if request.method == 'GET':
        form = RegisterForm()
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username, password=password)
            return HttpResponseRedirect(reverse('login'))

    context['form'] = form
    return render(request, 'chat/register.html', context=context)
