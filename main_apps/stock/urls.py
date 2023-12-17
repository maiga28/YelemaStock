from . import views
from django.urls import path

app_name = 'stock'

urlpatterns = [
  
    path('ajouter_produit/', views.ajouter_produit, name='ajouter_produit'),
    path('modifier_produit/<int:pk>/', views.modifier_produit, name='modifier_produit'),
    path('supprimer_produit/<int:pk/', views.supprimer_produit, name='supprimer_produit')
    
]