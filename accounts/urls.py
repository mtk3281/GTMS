# GTMS/urls.py

from django.urls import path
from accounts import views as accounts_views

urlpatterns = [
    path('verify/<uidb64>/<token>/', accounts_views.verify_email_view, name='email_verification'),
    path('verify/<uidb64>/<token>', accounts_views.verify_email_view),
    path('profile-creation/<uuid:user_id>/', accounts_views.profile_creation_view, name='profile_creation'),
    path('', accounts_views.home, name='home'),
    path('login/', accounts_views.login_view, name='login'),
    path('email/', accounts_views.email_entry_view, name='email_entry'),
    path('email-verification-sent/', accounts_views.email_verification_sent_view, name='email_verification_sent'),
    # path('create-profile/', accounts_views.profile_creation_view, name='profile_creation'),
    path('logout/', accounts_views.logout_view, name='logout'),
]
