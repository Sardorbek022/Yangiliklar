from django import forms
from django.contrib.auth.models import User

from .models import ProfileModel

class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField()
    password_2 = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        widgets = {
            'username': forms.TextInput(),
            'first_name': forms.TextInput(),
            'email': forms.EmailInput(),
        }
        
    def clean_password_2(self):
        data = self.cleaned_data
        if data['password'] != data['password_2']:
            raise forms.ValidationError("2 ta parol bir xil bo'lishi kerak")
        return data['password_2']


class UserEditForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
        
class ProfileEditForm(forms.ModelForm):
    
    class Meta:
        model = ProfileModel
        fields = ['photo', 'date_of_birth', 'address']

