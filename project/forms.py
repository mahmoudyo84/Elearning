from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Users
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password



class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['Username', 'password', 'Name', 'Email', 'RoleID']


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user = Users.objects.get(Username=username)

                if not check_password(password, user.password):
                    raise forms.ValidationError("Invalid password. Please try again.")

                if not user.is_active:
                    raise forms.ValidationError("This account is inactive.")

                self.user = user  # Store the user instance for later use

            except Users.DoesNotExist:
                raise forms.ValidationError("Username does not exist.")

        return cleaned_data

    def get_user(self):
        return getattr(self, 'user', None)