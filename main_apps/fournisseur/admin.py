from django.contrib import admin
from .models import Fournisseur,Fournir_Produit,Fournir_Stock

class FournisseurAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom','adresse', 'telephone')
    list_filter = ('nom','adresse', 'telephone')
    search_fields = ['Fournisseur__nom']
    
admin.site.register(Fournisseur, FournisseurAdmin)



class Fournir_ProduitAdmin(admin.ModelAdmin):

    list_filter = ('id', 'fournisseur', 'produit', 'stock')
    list_display = ('id', 'fournisseur', 'produit', 'stock')
    search_fields = ['fournisseur__nom', 'produit','stock']  # Assurez-vous d'ajuster cela en fonction de votre modèle
    

admin.site.register(Fournir_Produit, Fournir_ProduitAdmin)
# Register your models here.
