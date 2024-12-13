from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Users
from django.contrib.auth.hashers import make_password


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['Username', 'Password', 'Name', 'Email', 'RoleID']

    # Custom password field
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data.get('Password')
        if password:
            return make_password(password)
        return password


class LoginForm(AuthenticationForm):
    class Meta:
        model = Users
        fields = ['Username', 'Password']