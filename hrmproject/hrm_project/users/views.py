from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated



class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(UserLoginView, self).post(request, *args, **kwargs)
        token = response.data.get('token')
        if token:
            user_token = get_object_or_404(Token, key=token)
            user = user_token.user
            serializer = UserSerializer(user)
            return Response({
                'token': token,
                'user': serializer.data
            })
        else:
            return Response({'error': 'Token not found'}, status=status.HTTP_400_BAD_REQUEST)

