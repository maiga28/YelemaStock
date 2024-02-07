from . import views
from django.urls import path
from .views import supprimer_produit
from .views import custom_page_not_found


app_name = 'stock'

urlpatterns = [
  
    path('ajouter_produit/', views.ajouter_produit, name='ajouter_produit'),
    path('modifier_produit/<int:pk>/', views.modifier_produit, name='modifier_produit'),
  # Corrected URL pattern
    path('stock/supprimer_produit/<int:pk>/', supprimer_produit, name='supprimer_produit'),
    
]

# Ajoutez un pattern générique pour gérer les URL non correspondantes
urlpatterns += [
    path('<path:unknown_path>', custom_page_not_found),
]
