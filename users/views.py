from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics,status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group
from rest_framework.response import Response
from.models import *
from .serializers import *
from django.contrib.auth.hashers import check_password
# Create your views here.

class UsersView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()


        token,created = Token.objects.get_or_create(user=user)
        group_name = 'client'
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
        response_data = serializer.data
        response_data['token'] = token.key
        return Response(response_data,status=status.HTTP_201_CREATED)


class Login(generics.CreateAPIView):
    # queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        # print(serializer)
        # user = serializer.save()

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = CustomUser.objects.filter(email=email).first()
        # print(email)
        if user and check_password(password, user.password):
            token, created = Token.objects.get_or_create(user=user)
            user_serializer = UserSerializer(user)
            return Response({
                'token': token.key,
                'user': user_serializer.data,
                }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class AppVersionApi(generics.ListCreateAPIView):
    queryset = AppVersion.objects.all()
    serializer_class = AppVersionSerializer