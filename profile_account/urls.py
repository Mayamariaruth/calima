from django.urls import path
from .views import profile_account


urlpatterns = [
    path('profiles/profile/', profile_account, name='profile_account'),
]