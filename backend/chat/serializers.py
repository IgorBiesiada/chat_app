from rest_framework import serializers
from rest_framework.serializers import ListSerializer
from chat.models import ChatRoom


class CreateRoomSerializer(serializers.Serializer):
    class Meta:
        model = ChatRoom
        fields = ['chatroom_name', 'is_public']

class PublicRoomListSerializer(serializers.Serializer):
    
    class Meta:
        model = ChatRoom
        