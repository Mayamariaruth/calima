from django.urls import path
from . import views


urlpatterns = [
    path('accounts/delete/', views.delete_account, name='delete_account'),
    path('accounts/delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('accounts/edit-booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('accounts/edit/', views.edit_details, name='edit_details'),
    path('accounts/profile/', views.profile_account, name='profile_account'),
]
