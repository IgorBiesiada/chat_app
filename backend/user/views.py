from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from user.serializers import UserSerializer, RegisterSerializer, LoginSerializer, AddFriendSerializer
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CreateUserView(CreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RegisterSerializer

class LoginUserView(TokenObtainPairView):
    serializer_class = LoginSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class AddFriendView(CreateAPIView):
    serializer_class = AddFriendSerializer
    authentication_classes = [JWTAuthentication]
    permissions_classes = [IsAuthenticated]
