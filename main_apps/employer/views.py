from django.shortcuts import render, get_object_or_404, redirect
from .models import Employer, Poste
from main_apps.client.models import Client, Commande
from main_apps.facture.models import Facture
from main_apps.fournisseur.models import Fournisseur, Fournir_Produit
from main_apps.note_frais.models import Note_frais
from .forms import ClientForm, ClientUpdateForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

# Importez vos modèles ici
from main_apps.employer.models import Employer, Poste

from django.shortcuts import render, get_object_or_404, redirect
from .models import Employer, Poste
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Employer, Poste
from django.contrib.auth.decorators import login_required

from rolepermissions.decorators import has_role_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model

User = get_user_model()
@login_required
@user_passes_test(lambda u: u.groups.filter(name='Gestionnaire').exists() or u.groups.filter(name='Employer').exists())
def dash_employer(request):
    # Récupérer l'employeur associé à l'utilisateur connecté
    try:
        employer = Employer.objects.get(username=request.user.username)
    except Employer.DoesNotExist:
        employer = None

    # Si l'employeur est trouvé, récupérer les postes associés
    if employer:
        postes = Poste.objects.filter(employer=employer)
    else:
        postes = None

    context = {
        'user': request.user,
        'employer': employer,
        'postes': postes,
    }

    return render(request, 'employer/dash_employer.html', context)







def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            # Enregistrez le nouveau client dans la base de données
            try:
                client = Client.objects.create(
                    name=name,
                    email=email,
                )
                return redirect('employer:dash_employer')
            except Exception as e:
                print("Erreur lors de l'enregistrement du client :", e)
                # Vous pouvez ajouter d'autres messages de débogage si nécessaire
        else:
            print("Formulaire invalide :", form.errors)
    else:
        form = ClientForm()
        context = {'form': form}
    
    return render(request, 'employer/employer.html', context)

def update_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    
    if request.method == 'POST':
        form = ClientUpdateForm(request.POST, instance=client)
        
        if form.is_valid():
            form.save()
            return redirect('employe:dash_employer')
    else:
        form = ClientUpdateForm(instance=client)  # Remplir le formulaire avec les données existantes

    return render(request, 'employer/update_client.html', context={'form': form})

def supprimer_client(request):
    return render(request, 'employer/supprimer_client.html')

def employer_profile(request):
    employers = Employer.objects.all()
    context = {
        'employers': employers,
    }
    return render(request, 'employer_profile.html', context)

def custom_page_not_found(request, unknown_path):
    return render(request, 'gestion/404.html', {'unknown_path': unknown_path}, status=404)
