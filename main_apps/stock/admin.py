from django.contrib import admin
from .models import Produit,Stock
# Register your models here.
@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'slug','prix', 'stock', 'date_ajout')
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('produit','quantite','type_mouvement')