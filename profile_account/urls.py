from django.urls import path
from . import views


urlpatterns = [
    path('accounts/profile/', views.profile_account, name='profile_account'),
]