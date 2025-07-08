from django.urls import include, path
from rest_framework import routers
from user.views import UserViewSet, CreateUserView

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', CreateUserView.as_view(), name='register')
]
