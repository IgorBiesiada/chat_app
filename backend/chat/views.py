from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from chat.serializers import CreateRoomSerializer, PublicRoomListSerializer 
from rest_framework import viewsets
from chat.models import ChatRoom
from rest_framework.response import Response
# Create your views here.


class CreateRoomView(CreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = CreateRoomSerializer

class PublicChatViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.filter(is_public=True)
    serializer = PublicRoomListSerializer
        