from django.urls import path, include
from . import views


urlpatterns = [
    path('accounts/profile/', views.profile_account, name='profile_account'),
    path('accounts/delete/', views.delete_account, name='delete_account'),
    path('accounts/edit/',views.edit_details, name='edit_details'),
]