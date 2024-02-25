from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from django.urls import path, include
from menu.views import menu_page


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('menu/', menu_page, name="menu_page"),
    path('', include('booking.urls'), name='booking_urls'),
    path('', include('home.urls'), name='home_urls'),
    path('', include('profile_account.urls'), name='profile_urls'),
]


admin.site.unregister(Site)
admin.site.unregister(Group)
