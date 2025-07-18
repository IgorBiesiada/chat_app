from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from chat.serializers import CreateRoomSerializer
# Create your views here.


class CreateRoomView(CreateAPIView):
    serializer_class = CreateRoomSerializer
    