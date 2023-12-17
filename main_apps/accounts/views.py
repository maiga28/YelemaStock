from .forms import SignUpForm, LoginForm  # Assurez-vous d'importer le formulaire approprié depuis votre application
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import authenticate, login
from .forms import LoginForm  # Replace '.forms' with the correct path to your LoginForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.http import HttpResponseNotFound
from .forms import LoginForm  # Assurez-vous d'ajuster le chemin en fonction de la structure de votre projet
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from main_apps.stock.models import Produit,Stock
User = get_user_model()

def send_verification_email(request, user):
    # Générez le token unique pour la vérification de l'e-mail
    token = default_token_generator.make_token(user)

    # Encodez l'ID utilisateur pour être utilisé dans l'URL
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

    # Construisez l'URL de vérification avec le lien unique
    verification_url = request.build_absolute_uri(reverse('accounts:verify_email', args=[uidb64, token]))
    

    # Personnalisez le contenu de l'e-mail de vérification avec le lien unique
    subject = 'Email Verification'
    message = f'Please verify your email address by clicking on the link: {verification_url}'
    from_email = 'tdjangosite@gmail.com'  # Remplacez par votre adresse e-mail ou utilisez une dédiée pour envoyer des e-mails
    to_email = user.email

    # Envoyez l'e-mail avec le lien de vérification unique
    send_mail(subject, message, from_email, [to_email], fail_silently=False)


    
#def activateEmail(request, user, to_email):
#    messages.success(request, f'Dear <b>{user}</b>, please go to your email <b>{to_email}</b> inbox and click on\
#       recieved activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder. ')

# Create your views here.
def register(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            # Utilisez create_user pour créer un utilisateur avec un mot de passe hashé
            user = User.objects.create_user(username=email, email=email, password=password)

            # Générez le token unique pour la vérification de l'e-mail
            token = default_token_generator.make_token(user)

            # Encodez l'ID utilisateur pour être utilisé dans l'URL
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

            # Construisez l'URL de vérification avec le lien unique
            verification_url = request.build_absolute_uri(reverse('accounts:verify_email', args=[uidb64, token]))

            # Envoyez l'e-mail avec le lien de vérification unique
            send_verification_email(request, user)

            msg = 'User created successfully. Please check your email for verification.'
            success = True
            return redirect('accounts:verify_email', user_id=uidb64, token=token)

    else:
        # Le reste de votre code existant pour la gestion de la requête GET
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


User = get_user_model()

@login_required
def verify_email(request, user_id, *args, **kwargs):
    # Function code here
    if request.user.email_verified:
        # L'e-mail est déjà vérifié, redirigez l'utilisateur vers une page appropriée
        return redirect('gestion:home')  # Remplacez 'home' par le nom de votre vue d'accueil

    if request.method == 'GET':
        return render(request, 'account/verify_email.html')

    elif request.method == 'POST':
        # Marquer l'e-mail comme vérifié
        request.user.email_verified = True
        request.user.save()
        return redirect('gestion:home')  # Remplacez 'home' par le nom de votre vue d'accueil

# Dans votre vue d'inscription

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)

                # Rediriger en fonction du groupe de l'utilisateur
                if user.groups.filter(name='Gestionnaire').exists():
                    return redirect("accounts:dash_gestionnaire")
                elif user.groups.filter(name='Comptable').exists():
                    return redirect("accounts:dash_comptable")
                elif user.groups.filter(name='Assistant').exists():
                    return redirect("accounts:dash_assistant")
                else:
                    # Redirection par défaut s'il n'appartient à aucun groupe spécifique
                    return redirect("gestion:home")
            else:
                msg = 'Identifiants invalides'
        else:
            msg = 'Données du formulaire non valides. Veuillez vérifier vos saisies.'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

def logout(request):
    return render(request, 'accounts/logout.html')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Gestionnaire').exists())
def dash_gestionnaire(request):
    produits = Produit.objects.all()
    quantite_produit = Stock.objects.all()
    context ={
        'produits': produits,
        'quantite_produit':quantite_produit
    }
    return render(request, 'gestion/dash_gestionnaire.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Comptable').exists())
def dash_comptable(request):
    return render(request, 'gestion/dash_comptable.html')


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Assistant').exists())
def dash_assistant(request):
    return render(request, 'gestion/dash_assistant.html')