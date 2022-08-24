from django.db import models

# Create your models here.
class bank(models.Model):
    name = models.CharField(max_length=250)
    DOB = models.DateField()
    AGE = models.IntegerField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=100)
    mail = models.EmailField(max_length=250)
    adress = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    materials = models.CharField(max_length=100)

    def __str__(self):
        return self.name
