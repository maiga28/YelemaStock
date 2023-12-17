from . import views
from django.urls import path

app_name = 'gestion'

urlpatterns = [
  
    path('', views.home, name='home'),

]