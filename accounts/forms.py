from accounts.models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.models import U

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args , **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'h-full-width', 'placeholder': 'Username', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'h-full-width',
            'placeholder': 'Password',
            'id': 'password',
        }
))

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'h-full-width', 'placeholder': 'Username', 'id': 'username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'h-full-width', 'placeholder': 'First Name', 'id': 'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'h-full-width', 'placeholder': 'Last Name', 'id': 'last_name'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'h-full-width', 'placeholder': 'Phone', 'id': 'phone'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'h-full-width', 'placeholder': 'Address', 'id': 'address'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'h-full-width', 'placeholder': 'Email', 'id': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput({'class': 'h-full-width', 'placeholder': 'Password', 'id': 'password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone', 'address', 'email', 'password']

class ProfileEditForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'h-full-width', 'placeholder': 'Phone', 'id': 'phone'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'h-full-width', 'placeholder': 'Address', 'id': 'address'}))

    class Meta:
        model = Profile
        fields = ['phone', 'address']


class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'h-full-width', 'placeholder': 'Username', 'id': 'username', 'readonly': True}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'h-full-width', 'placeholder': 'First Name', 'id': 'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'h-full-width', 'placeholder': 'Last Name', 'id': 'last_name'}))

    class Meta:
        fields = ['username', 'first_name', 'last_name']
        model = User
