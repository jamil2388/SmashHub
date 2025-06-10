from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        PLAYER = "PLAYER", "Player"
        CLUB_OWNER = "CLUB_OWNER", "Club Owner"

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.PLAYER)
