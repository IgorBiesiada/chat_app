from django.urls import include, path
from rest_framework import routers
from user.views import UserViewSet, CreateUserView, LoginUserView, AddFriendView

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('add-friend/', AddFriendView.as_view(), name='add-friend')
]
