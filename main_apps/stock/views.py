
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

from django.shortcuts import render,redirect
from .models import Produit,Stock
from .forms import ProduitForm
from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.shortcuts import render, redirect
from .forms import ProduitForm,Produit_Modifier_Form  # Assurez-vous que l'import est correct

User = get_user_model()


def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)  # N'oubliez pas de passer request.FILES pour traiter les fichiers
        if form.is_valid():
            nom = form.cleaned_data['nom']
            description = form.cleaned_data['description']
            slug = form.cleaned_data['slug']
            image = form.cleaned_data['image']
            prix = form.cleaned_data['prix']

            try:
                produit = Produit.objects.create(
                    nom=nom,
                    description=description,
                    slug=slug,
                    image=image,
                    prix=prix,
                    # N'oubliez pas de définir la quantité initiale du stock ici si nécessaire
                )

                return redirect('gestion:home')
            except Exception as e:
                print("Erreur lors de l'enregistrement du produit :", e)
                # Vous pouvez ajouter des messages de débogage si nécessaire
        else:
            print("Formulaire invalide :", form.errors)
    else:
        form = ProduitForm()

    context = {'form': form}
    return render(request, 'stock/ajouter_produit.html', context)


    
def modifier_produit(request,pk):
    
    produit = get_object_or_404(Produit,id=pk)
    
    if request.method == 'POST':
        
        form = Produit_Modifier_Form(request.POST,  instance=produit)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('gestion:home') 
    else:
        
        form = Produit_Modifier_Form()  # Remplir le formulaire avec les données existantes

    return render(request, 'stock/modifier_produit.html', context={'form': form})


def supprimer_produit(request,pk):
    
    produit = get_object_or_404(Produit,id=pk)
    
    if request.method == 'POST':
        produit.delete()
        return redirect('gestion:home')  
    
    return render(request,'stock/supprimer_produit.html', context={'produit': produit})

def custom_page_not_found(request, unknown_path):
    return render(request, 'gestion/404.html', {'unknown_path': unknown_path}, status=404)

