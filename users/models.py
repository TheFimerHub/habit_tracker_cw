from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    telegram_chat_id = models.CharField(max_length=100, blank=True, null=True)
