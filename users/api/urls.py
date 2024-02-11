from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from django.urls import path
from users.api.views.usersView import (
    RegisterUserView,
    CurrentUserView,
)


app_name = 'users'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user-register'),
    path('me/', CurrentUserView.as_view(), name='user-me'),
]


urlpatterns.extend(
    [
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    ]
)
