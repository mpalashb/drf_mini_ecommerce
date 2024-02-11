from rest_framework import generics, response, status, permissions, views
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.api.serializers.userSerializers import (
    UserSerializer,
    UserRegisterSerializer,

)


class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)


class CurrentUserView(generics.GenericAPIView):
    serializer_class = UserSerializer

    authentication_classes = (
        JWTAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance=request.user)

        return response.Response(serializer.data, status=status.HTTP_200_OK)
