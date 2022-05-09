from django.shortcuts import render

# Create your views here.

from django.conf import settings
from django.shortcuts import render
from datetime import datetime, timedelta
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from backend.permissions import IsAuthor
from users.models import CommunityUser
from users.serializers import IsAuthorSerializer, LoginSerializer, UserSerializer, RegisterSerializer, ProfileSerializer
import jwt
# Create your views here.


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = CommunityUser.objects.all()
    serializer_class = RegisterSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()

    #     return Response({
    #         "user": UserSerializer(user, context=self.get_serializer_context()).data,
    #         "message": "User created successfully!"
    #     })


class LoginView(generics.GenericAPIView):
    queryset = CommunityUser.objects.all()
    serializer_class = LoginSerializer

    # def post(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     username = request.data.get('username')
    #     password = request.data.get('password')

    #     try:
    #         user_to_login = CommunityUser.objects.get(username=username)
    #     except CommunityUser.DoesNotExist:
    #         raise PermissionDenied(detail='Unauthorized')

    #     if not user_to_login.check_password(password):
    #         raise PermissionDenied(detail='Unauthorized')

    #     expiry_time = datetime.now() + timedelta(days=7)
    #     token = jwt.encode({
    #         'sub': user_to_login.id,
    #         'exp': int(expiry_time.strftime('%s'))
    #     },
    #         settings.SECRET_KEY,
    #         algorithm='HS256'
    #     )

    #     return Response({
    #         'token': token,
    #         'message': f'Welcome back {username}'
    #     }, status=status.HTTP_200_OK)


class ProfileView(generics.ListAPIView):
    queryset = CommunityUser.objects.all()
    serializer_class = UserSerializer


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = CommunityUser.objects.all()
    serializer_class = ProfileSerializer


class ProfileUpdateDetailView(generics.RetrieveUpdateDestroyAPIView):
    permmission_classes = [IsAdminUser | IsAuthor]
    queryset = CommunityUser.objects.all()
    serializer_class = ProfileSerializer


class IsAuthorView(generics.RetrieveUpdateDestroyAPIView):

    queryset = CommunityUser.objects.all()
    serializer_class = IsAuthorSerializer


class IsAuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommunityUser.objects.all()
    serializer_class = IsAuthorSerializer
