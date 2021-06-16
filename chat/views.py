from django.shortcuts import render


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
