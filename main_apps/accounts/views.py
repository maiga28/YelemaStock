from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from django.http import HttpResponseNotFound
from .forms import SignUpForm, LoginForm

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

@login_required
def verify_email(request, user_id, token):
    if request.user.email_verified:
        # L'e-mail est déjà vérifié, redirigez l'utilisateur vers une page appropriée
        return redirect('gestion:home')  # Remplacez 'home' par le nom de votre vue d'accueil

    if request.method == 'POST':
        # Marquer l'e-mail comme vérifié
        request.user.email_verified = True
        request.user.save()
        return redirect('gestion:home')  # Remplacez 'home' par le nom de votre vue d'accueil

    return HttpResponse(f"Verification for user {user_id} with token {token}")

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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Dans views.py de main_apps/accounts

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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

                # Affichez des informations de débogage
                user_groups = user.groups.values_list('name', flat=True)
                print("User Groups:", user_groups)

                # Redirection en fonction des groupes
                if 'Gestionnaire' in user_groups:
                    print("Redirecting to gestion:home")
                    return redirect("gestion:home")
                elif 'Comptable' in user_groups:
                    print("Redirecting to GRH:drh_view")
                    return redirect("GRH:drh_view")
                elif 'Assistant' in user_groups:
                    print("Redirecting to accounts:dash_assistant")
                    return redirect("accounts:dash_assistant")
                elif 'Employer' in user_groups:
                    print("Redirecting to employer:dash_employer")
                    return redirect("employer:dash_employer")
                else:
                    print("Redirecting to client:home")
                    return redirect("client:home")

            else:
                msg = 'Identifiants invalides'
        else:
            msg = 'Données du formulaire non valides. Veuillez vérifier vos saisies.'

    # Récupérer la valeur de 'next' de la requête
    next_url = request.POST.get('next', request.GET.get('next', ''))

    return render(request, "accounts/login.html", {"form": form, "msg": msg, "next_url": next_url})





def logout(request):
    return render(request, 'accounts/logout.html')

def custom_page_not_found(request, unknown_path):
    return render(request, 'gestion/404.html', {'unknown_path': unknown_path}, status=404)
