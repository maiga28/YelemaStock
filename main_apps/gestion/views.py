from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from django.shortcuts import render
from main_apps.stock.models import Produit, Stock
from rolepermissions.decorators import has_role_decorator
from .models import Gestionnaire  


User = get_user_model()
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from main_apps.stock.models import Produit, Stock
from django.shortcuts import render

User = get_user_model()

from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import Gestionnaire  # Assurez-vous d'importer correctement votre modèle Gestionnaire
from main_apps.stock.models import Produit, Stock

def is_gestionnaire(user):
    return user.groups.filter(name='Gestionnaire').exists()

@login_required
@user_passes_test(is_gestionnaire, login_url='/client/client-view/')
def home(request):
    try:
        gestionnaire = Gestionnaire.objects.get(username=request.user.username)
    except Gestionnaire.DoesNotExist:
        gestionnaire = None
    
    produits = Produit.objects.all()
    quantite_produit = Stock.objects.all()
    
    context = {
        'user': request.user,
        'produits': produits,
        'quantite_produit': quantite_produit,
        'gestionnaire': gestionnaire
    }
    
    return render(request, 'gestion/home.html', context)

def custom_access_denied(request, unknown_path):
    return render(request, 'gestion/404.html', {'unknown_path': unknown_path}, status=404)



def custom_page_not_found(request, unknown_path):
    return render(request, 'gestion/404.html', {'unknown_path': unknown_path}, status=404)
