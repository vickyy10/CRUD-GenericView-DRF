from django.db import models

# Create your models here.


class Doctor(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=100)



    def __str__(self):
        return self.name