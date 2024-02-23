from django import forms
from django.contrib.auth.models import User


# Create your forms here.
class EditForm(forms.ModelForm):
    """
    Edit account details form
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)
        help_texts = {
            'email': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        instance = self.instance

        if username and username != instance.username:
            if User.objects.filter(username=username).exists():
                    self.add_error('username', 'This username is already in use.')
        if email and email != instance.email:
            if User.objects.filter(email=email).exists():
                    self.add_error('email', 'This email is already in use.')
    
        return cleaned_data
