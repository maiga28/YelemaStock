from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, default='', blank=False)  # Mettez à jour ici
    image = models.ImageField(upload_to='image/', blank=False)  # Mettez à jour ici
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_ajout = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['-date_ajout']
        verbose_name = "produit"
        verbose_name_plural = "produits"

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

from django.db import models
from main_apps.stock.models import Produit

class Stock(models.Model):
    produit = models.OneToOneField(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField(
        default=0,  # Vous pouvez ajuster la valeur par défaut selon vos besoins
        help_text="La quantité en stock"
    )
    type_mouvement = models.CharField(
        max_length=1,
        choices=[('E', 'Entrée'), ('S', 'Sortie')],
        default='E',
        help_text="Type de mouvement (Entrée ou Sortie)"
    )
    date_mouvement = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_mouvement']
        verbose_name = "mouvement de stock"
        verbose_name_plural = "mouvements de stock"

    def __str__(self):
        return f"{self.produit.nom} - Stock: {self.quantite}"

    def update_stock(self, quantite):
        self.quantite -= quantite
        self.save()
