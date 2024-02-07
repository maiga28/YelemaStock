
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.http import HttpResponseNotFound

from django.shortcuts import render
from main_apps.stock.models import Produit,Stock
from django.contrib.auth.decorators import login_required, user_passes_test

User = get_user_model()


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Gestionnaire').exists())
def home(request):
    
    produits = Produit.objects.all()
    quantite_produit = Stock.objects.all()
    
    context = {
        
        'produits': produits,
        'quantite_produit':quantite_produit
        
    }
    
    return render(request, 'gestion/home.html', context)


def custom_page_not_found(request, unknown_path):
    return render(request, 'gestion/404.html', {'unknown_path': unknown_path}, status=404)
