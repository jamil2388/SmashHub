from django.urls import path
from .views import PlayerSignupView, ClubSignupView
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('signup/player/', PlayerSignupView.as_view(), name='player-signup'),
    path('signup/club/', ClubSignupView.as_view(), name='club-signup'),

    # jwt login
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
