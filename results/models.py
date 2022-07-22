from django.db import models


class Result(models.Model):
    concurso = models.IntegerField(primary_key=True)
    data = models.DateField()
    bola1 = models.IntegerField()
    bola2 = models.IntegerField()
    bola3 = models.IntegerField()
    bola4 = models.IntegerField()
    bola5 = models.IntegerField()
    bola6 = models.IntegerField()
