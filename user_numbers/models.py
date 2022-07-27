from django.db import models
from uuid import uuid4


class UserNumbersModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    numbers = models.CharField(max_length=100)

    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="user_numbers"
    )
