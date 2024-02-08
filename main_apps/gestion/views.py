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

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Gestionnaire').exists() or u.groups.filter(name='Employer').exists())
def home(request):
    # Récupérer l'utilisateur connecté
    user = request.user
    
    # Récupérer tous les produits
    produits = Produit.objects.all()
    
    # Récupérer toutes les quantités de produits
    quantite_produit = Stock.objects.all()
    
    context = {
        'user': user,
        'produits': produits,
        'quantite_produit': quantite_produit
    }
    
    return render(request, 'gestion/home.html', context)


def custom_page_not_found(request, unknown_path):
    return render(request, 'gestion/404.html', {'unknown_path': unknown_path}, status=404)
