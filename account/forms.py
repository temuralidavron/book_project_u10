from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=[
            'username',
            'password',

        ]

    def save(self, commit=True,**kwargs):
        return CustomUser.objects.create_user(
            username=self.cleaned_data.get('username'),
            password=self.cleaned_data.get('password'),
        )




class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)
