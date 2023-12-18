

from django.shortcuts import render
from main_apps.stock.models import Produit,Stock
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
@login_required
def home(request):
    
    produits = Produit.objects.all()
    quantite_produit = Stock.objects.all()
    
    context ={
        'produits': produits,
        'quantite_produit':quantite_produit
    }
    
    return render(request, 'gestion/home.html', context)
