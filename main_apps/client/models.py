from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator
from main_apps.stock.models import Produit,Stock


# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit, through='LigneCommande')
    date_commande = models.DateField(auto_now_add=True)
    statut_livraison = models.CharField(
        max_length=50,
        choices=[('en_attente', 'En attente'), ('en_cours', 'En cours'), ('livree', 'Livré')],
        default='en_attente'
    )

    def __str__(self):
        return f"Commande {self.pk} - {self.client}"

    def calculer_prix_total(self):
        lignes_commande = self.lignecommande_set.all()
        prix_total = sum(ligne.produit.prix * ligne.quantite for ligne in lignes_commande)
        return prix_total
    
class LigneCommande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    
    def __str__(self):
        return f"Ligne de commande {self.produit.nom} - {self.produit.nom}"

    def save(self, *args, **kwargs):
        # Récupérer le prix du produit associé
        self.produit.prix  # Assurez-vous que le champ prix existe dans le modèle Produit

        super().save(*args, **kwargs)

        # Mettre à jour le stock après l'enregistrement de la ligne de commande
        stock, created = Stock.objects.get_or_create(produit=self.produit)

        if stock:
            # Vous devrez ajuster cette partie en fonction de la logique spécifique
            stock.update_stock(self.quantite)