

# Register your models here.
from django.contrib import admin
from .models import Employer, Poste

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'address')
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['address']

class PosteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ['title']
    # Ajoutez d'autres options d'administration si nécessaire

admin.site.register(Employer, EmployerAdmin)
admin.site.register(Poste, PosteAdmin)
