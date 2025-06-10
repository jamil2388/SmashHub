from rest_framework import generics
from .serializers import PlayerSignupSerializer, ClubSignupSerializer
from .models import CustomUser

class PlayerSignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PlayerSignupSerializer

class ClubSignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ClubSignupSerializer
