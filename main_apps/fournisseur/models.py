from django.db import models
from main_apps.stock.models import Produit,Stock

# Create your models here.
class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "fournisseur"
        verbose_name_plural = "fournisseurs"
        
class Fournir_Produit(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name ='fournir_stock')

class Fournir_Stock(models.Model):
    pass
