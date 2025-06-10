from django.urls import path
from .views import PlayerSignupView, ClubSignupView

urlpatterns = [
    path('signup/player/', PlayerSignupView.as_view(), name='player-signup'),
    path('signup/club/', ClubSignupView.as_view(), name='club-signup'),
]
