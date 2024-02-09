from django.contrib import admin

# Register your models here.
from .models import Gestionnaire

class GestionnaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')  # Ajoutez d'autres champs si nécessaire
# Assurez-vous que 'id' et 'email' correspondent aux champs réels de votre modèle

    def first_name(self, obj):
        return obj.first_name

    def last_name(self, obj):
        return obj.last_name



admin.site.register(Gestionnaire, GestionnaireAdmin)