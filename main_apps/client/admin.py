from django.contrib import admin
from .models import Client, Commande, LigneCommande

class LigneCommandeInline(admin.TabularInline):
    model = LigneCommande
    extra = 1

class CommandeAdmin(admin.ModelAdmin):
    inlines = [LigneCommandeInline]
    list_display = ('id', 'client', 'date_commande', 'statut_livraison', 'calculer_prix_total')
    list_filter = ('statut_livraison',)
    search_fields = ['client__name']

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'adresse', 'telephone', 'email')
    search_fields = ['name', 'email']

class LigneCommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'produit', 'commande', 'quantite')
    search_fields = ['produit__nom', 'commande__client__name']  # Assurez-vous d'ajuster cela en fonction de votre modèle
    


admin.site.register(Client, ClientAdmin)
admin.site.register(Commande, CommandeAdmin)
admin.site.register(LigneCommande, LigneCommandeAdmin)
