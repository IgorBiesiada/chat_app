from django.urls import path, include
from chat.views import CreateRoomView, PublicChatViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'chat-list', PublicChatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-room/', CreateRoomView.as_view(), name='create-room'),

]
 

