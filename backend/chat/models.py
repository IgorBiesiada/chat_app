from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Chat(models.Model):
    message_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_sender')
    message_recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_recipient')
    message = models.CharField(max_length=500)
    send_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class ChatRoom(models.Model):
    chatroom_name = models.CharField(max_length=50)
    participants = models.ManyToManyField(User, related_name='chat_rooms')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

class Messages(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='room_messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room_sender')
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)