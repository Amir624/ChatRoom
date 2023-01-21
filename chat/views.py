from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .models import Chat

def index(request):
    user = request.user
    chat_room = Chat.objects.filter(members=user)

    return render(request, 'chat/index.html', {'chat_rooms': chat_room})


def room(request, room_name):
    username = request.user.username
    user = request.user
    chat_model = Chat.objects.filter(roomname=room_name)

    if not chat_model.exists():
        chat = Chat.objects.create(roomname=room_name)
        chat.members.add(user)
    else:
        chat_model[0].members.add(user)
    context = {'room_name': room_name, 'username':mark_safe(json.dumps(username))}
    return render(request, 'chat/room.html', context )
