from django.urls import path
from . import views
from .views import verify_email
from .views import custom_page_not_found


from django.urls import path
from .views import login_view, register, logout, verify_email, send_verification_email, custom_page_not_found

app_name = 'accounts'

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('verification/<str:user>/<str:token>/', send_verification_email, name='email_verification'),
    path('verify_email/<str:user_id>/<slug:token>/', verify_email, name='verify_email'),
    
    # Ajoutez un pattern générique pour gérer les URL non correspondantes
    path('<path:unknown_path>', custom_page_not_found),
]

