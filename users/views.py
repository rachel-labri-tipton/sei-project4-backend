from django.shortcuts import render

# Create your views here.

from django.conf import settings
from django.shortcuts import render
from datetime import datetime, timedelta
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from backend.permissions import IsLoggedInUser
from users.models import CommunityUser
from users.serializers import LoginSerializer, ProfileEditSerializer, UserSerializer, RegisterSerializer
import jwt
# Create your views here.


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = CommunityUser.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    queryset = CommunityUser.objects.all()
    serializer_class = LoginSerializer


class ProfileView(generics.ListAPIView):
    queryset = CommunityUser.objects.all()
    serializer_class = UserSerializer


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = CommunityUser.objects.all()
    serializer_class = UserSerializer


class ProfileUpdateDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsLoggedInUser]
    queryset = CommunityUser.objects.all()
    serializer_class = ProfileEditSerializer
