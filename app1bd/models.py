from django.db import models

# Create your models here.


class Equipements(models.Model):
    Code_Equip = models.IntegerField(primary_key=True, unique=True)
    Designation = models.CharField(max_length=200, blank=True)
    Date_Ach = models.DateTimeField(auto_now_add=True)
    Date_mise_service = models.DateTimeField(auto_now_add=True)
    Carct_tech = models.CharField(max_length=300)
    Date_fin_garantie = models.DateTimeField(auto_now_add=True)
