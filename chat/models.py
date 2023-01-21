from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Chat(models.Model):
    roomname = models.CharField(max_length=50, blank=True)
    members = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.roomname


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    related_chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=True)
    timestamp = models.TimeField(auto_now_add=True)

    def last_message(self, roomname):
        return Message.objects.filter(related_chat__roomname=roomname).order_by('-timestamp')

    def __str__(self):
        return self.author.username
