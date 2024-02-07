"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from  .import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from .views import custom_page_not_found

# urls.py



urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('main_apps.gestion.urls')), 
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('main_apps.accounts.urls')),
    path('stock/', include('main_apps.stock.urls')),
    path('employer/', include('main_apps.employer.urls')),
    path('client/', include('main_apps.client.urls')),
    path('grh/', include('main_apps.GRH.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Ajoutez un pattern générique pour gérer les URL non correspondantes
urlpatterns += [
    path('<path:unknown_path>', custom_page_not_found),
]
