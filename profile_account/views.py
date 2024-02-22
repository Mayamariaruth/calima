from django.shortcuts import render


# Create your views here.
def profile_account(request):
    return render(request, 'profiles/profile.html')