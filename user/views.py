from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from user.serializers import UserSerializer, RegisterSerializer
from rest_framework.generics import CreateAPIView

# Create your views here.

class CreateUserView(CreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RegisterSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    