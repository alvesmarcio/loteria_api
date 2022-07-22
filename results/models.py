from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Result(models.Model):
    concurso = models.IntegerField(primary_key=True)
    data = models.DateField()
    bola1 = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(60)]
    )
    bola2 = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(60)]
    )
    bola3 = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(60)]
    )
    bola4 = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(60)]
    )
    bola5 = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(60)]
    )
    bola6 = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(60)]
    )
