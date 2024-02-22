def admin_user(request):
    """
    Context processor to make admin user available site-wide
    """
    is_admin = request.user.is_authenticated and request.user.is_staff
    return {'is_admin': is_admin}
