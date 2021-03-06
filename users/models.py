from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


class User(AbstractUser):
    id = models.CharField(
        primary_key=True, default=uuid4, editable=False, max_length=50
    )
    created_at = models.DateField(auto_now_add=True)

    objects = UserManager()
