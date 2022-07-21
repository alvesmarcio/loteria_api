from django.db import models
from uuid import uuid4

class UserNumbersModel(models.Model):
    id = models.AutoField(primary_key=True, default=uuid4)
    numbers = models.CharField(max_length=100)
    favorite = models.BooleanField(default=False)
    
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user_numbers')