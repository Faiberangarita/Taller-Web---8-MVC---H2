from django.db import models


class persona(models.Model):
    nombre = models.CharField(max_length=30)
    documento = models.IntegerField(max_length=15)


# Create your models here.
