from django.urls import path
from . import views

urlpatterns = [
    path('',views.drh_view, name='drh_view'),
]