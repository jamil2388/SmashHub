from rest_framework import generics
from .serializers import PlayerSignupSerializer, ClubSignupSerializer
from .models import CustomUser

# added for profile view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# added for logout view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

class PlayerSignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PlayerSignupSerializer

class ClubSignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ClubSignupSerializer

# return the profile view for users
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home_view(request):
    user = request.user

    # You can extend this to return PlayerProfile or Club info too
    user_data = {
        "id": user.id, # experimental
        "username": user.username,
        "email": user.email,
        "role": user.role,
    }

    return Response(user_data)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
