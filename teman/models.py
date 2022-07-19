from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models


class Teman(models.Model):
    nama = models.CharField(max_length=25)
    umur = models.IntegerField()
    alamat = models.TextField()
    foto = models.FileField()

    def __str__(self):
        return self.nama