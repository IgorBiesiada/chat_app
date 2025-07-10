from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

userModel = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = userModel
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class RegisterSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        user = userModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email']
        )

        return user
    
    class Meta:
        model = userModel
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class LoginSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)

        data['user_id'] = self.user.id
        data['username'] = self.user.username

        return data