

# Register your models here.
from django.contrib import admin
from .models import Employer, Poste
# Dans admin.py de main_apps/employer

from django.contrib import admin
from .models import Employer

# Dans admin.py de main_apps/employer

from django.contrib import admin
from .models import Employer

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')  # Ajoutez d'autres champs si nécessaire
# Assurez-vous que 'id' et 'email' correspondent aux champs réels de votre modèle

    def first_name(self, obj):
        return obj.first_name

    def last_name(self, obj):
        return obj.last_name



admin.site.register(Employer, EmployerAdmin)



class PosteAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ['title']
    # Ajoutez d'autres options d'administration si nécessaire


admin.site.register(Poste, PosteAdmin)
