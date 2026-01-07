from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=[
            'username',
            'password',

        ]



