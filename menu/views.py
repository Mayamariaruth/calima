from django.shortcuts import render

# Create your views here.
def menu_page(request):
    """
    Renders the menu template
    """
    return render(request, 'menu/menu.html')
