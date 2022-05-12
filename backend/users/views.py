from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, get_user_model

from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token

from .serializers import *


CustomUser = get_user_model()

@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    login_serializer = UserLoginSerializer(data=request.data)

    if not login_serializer.is_valid():
        return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(
        username=login_serializer.data['email'],
        password=login_serializer.data['password']
    )

    if user and user.is_active is False:
        return Response({'detail': 'User is not active!'},
                            status=status.HTTP_403_FORBIDDEN)

    if not user:
        return Response({'detail': 'Incorrect email or password!'},
                        status=status.HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)

    user_serialized = UserSerializer(user)

    return Response({
        'user': user_serialized.data,
        'token': token.key
    }, status=status.HTTP_200_OK)


class Registration(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = CustomUser.objects.all()


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response(status=status.HTTP_200_OK)

class UserListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    search_fields = ['email', 'first_name', 'last_name', 'username']

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    lookup_field = 'id' 