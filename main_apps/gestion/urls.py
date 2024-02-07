from django.urls import path
from .views import home, custom_page_not_found

app_name = 'gestion'

urlpatterns = [
    path('', home, name='home'),
]

# Ajoutez un pattern générique pour gérer les URL non correspondantes
urlpatterns += [
    path('<path:unknown_path>', custom_page_not_found),
]
