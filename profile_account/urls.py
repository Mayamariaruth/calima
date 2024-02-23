from django.urls import path
from . import views


urlpatterns = [
    path('profiles/profile/', views.profile_account, name='profile_account'),
]