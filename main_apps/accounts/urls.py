from django.urls import path
from . import views

app_name = 'accounts'  # Si vous utilisez un espace de noms

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
#   path('<str:user_id>/<str:token>/', views.verify_email, name='verify_email'),
    path('verification/<str:uidb64>/<str:token>/', views.send_verification_email, name='email_verification'),
    path('accounts/<int:user_id>/<str:token>/', views.verify_email, name='verify_email'),
############################################################################################################################   
    path('dash_gestionnaire/', views.dash_gestionnaire, name='dash_gestionnaire'),
    path('dash_comptable/', views.dash_comptable, name='dash_comptable'),
    path('dash_assistant/', views.dash_assistant, name='dash_assistant'),
]
