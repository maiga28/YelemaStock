from django.urls import path
from . import views

urlpatterns = [
   
   path('', views.client_view, name='client_view'),
   
   ]