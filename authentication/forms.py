from django import forms
from .models import CustomUser

class CustomUserInputForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'profile_pic']
        widgets = {'password': forms.PasswordInput(render_value=True)}

