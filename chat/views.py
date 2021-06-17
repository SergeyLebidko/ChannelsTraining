from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

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
        context['form'] = form
    return render(request, 'chat/register.html', context=context)
