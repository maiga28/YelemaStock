from functools import wraps
from django.shortcuts import render, redirect
from django.urls import reverse

def mon_deco(fonction_vue):
    @wraps(fonction_vue)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            # L'utilisateur est connecté, redirigez-le vers son tableau de bord
            return redirect("accounts:dash_gestionnaire")
        else:
            # L'utilisateur n'est pas connecté, laissez-le accéder à la vue normalement
            response = fonction_vue(request, *args, **kwargs)

            # Empêcher l'accès aux pages de connexion, d'inscription et d'accueil après la première connexion
            protected_paths = [reverse('login'), reverse('register'), reverse('home')]
            if request.path in protected_paths and request.user.is_authenticated:
                return redirect("accounts:dash_gestionnaire")  # Redirigez vers le tableau de bord après la première connexion

            return response

    return wrapper
