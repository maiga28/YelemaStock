from django.urls import path
from . import views
from .views import custom_page_not_found


app_name = 'employer'

urlpatterns = [
  #  path('', views.dash_employer, name='dash_employer'),
    path('ajouter_client/', views.ajouter_client, name='ajouter_client'),
    path('update_client/<int:client_id>/', views.update_client, name='update_client'),
    path('dash_employer/', views.dash_employer, name='dash_employer'),
]

# Ajoutez un pattern générique pour gérer les URL non correspondantes
urlpatterns += [
    path('<path:unknown_path>', custom_page_not_found),
]
