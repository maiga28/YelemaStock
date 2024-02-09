from django.shortcuts import render

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

# Create your views here.
User = get_user_model()
@login_required
def creer_facture(request): 
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            facture = form.save()  # Save the facture instance first

            for produit in form.cleaned_data['produits']:
                quantite = request.POST.get(f'quantite_produit_{produit.id}', 0)
                quantite = int(quantite)

                prix_unitaire = produit.price
                sous_total = quantite * prix_unitaire
                ligne_facture = LigneFacture(facture=facture, produit=produit, quantite=quantite, prix_unitaire=prix_unitaire, sous_total=sous_total)
                ligne_facture.save()

            return redirect('factures:liste_factures')
    else:
        form = FactureForm()
        
    clients = Client.objects.all()
    produits = Product.objects.all()
    factures = Facture.objects.all()

    context = {
        'clients': clients,
        'produits': produits,
        'factures': factures,
        'form': form,
    }

    return render(request, 'factures/creer_facture.html', context)
