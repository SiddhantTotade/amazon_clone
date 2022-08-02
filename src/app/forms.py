from dataclasses import fields
from importlib.metadata import files
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer, Product, Product_Img_Desktop


class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(
            attrs={'class': 'form-control'})}


class EditUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)
        help_texts = {
            'username': None,
        }


class EditUserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}))
    new_password1 = forms.CharField(label=('New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=('Confirm New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_('Email'), max_length=254, widget=forms.EmailInput(
        attrs={'autocomplete': 'email', 'class': 'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'locality',
                  'city', 'state', 'zipcode', 'country']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}), 'address': forms.TextInput(attrs={'class': 'form-control'}), 'locality': forms.TextInput(attrs={'class': 'form-control'}), 'city': forms.TextInput(
            attrs={'class': 'form-control'}), 'state': forms.Select(attrs={'class': 'form-control'}), 'zipcode': forms.NumberInput(attrs={'class': 'form-control'}), 'country': forms.Select(attrs={'class': 'form-control'})}


class UploadProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'selling_price', 'discounted_price',
                  'description', 'brand', 'category', 'product_image']
        widgets = {'product-name': forms.TextInput(attrs={'class': 'form-control'}), 'product-selling-price': forms.TextInput(attrs={'class': 'form-control'}),
                   'product-discounted-price': forms.TextInput(attrs={'class': 'form-control'}), 'product-description': forms.TextInput(attrs={'class': 'form-control'}),
                   'product-brand': forms.TextInput(attrs={'class': 'form-control'}), 'product-category': forms.TextInput(attrs={'class': 'form-control'}), 'product-image': forms.TextInput(attrs={'class': 'form-control'})}
