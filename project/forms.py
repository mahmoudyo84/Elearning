from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Users
from django.contrib.auth.hashers import make_password

'''
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
        '''
# blog/forms.py
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

# نموذج التسجيل
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    # التحقق من كلمه المرور
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("كلمتا المرور غير متطابقتين")
        
        # تحقق من قوة كلمة المرور (مثال: تحتوي على أحرف كبيرة وصغيرة وأرقام)
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password1):
            raise ValidationError("كلمة المرور يجب أن تحتوي على 8 أحرف على الأقل وتتضمن أحرفًا كبيرة وصغيرة وأرقامًا.")
        
        return password2

# نموذج الدخول
from django import forms
from blog import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

# نموذج ملف تعريف المستخدم
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'phone_number', 'is_instructor']
