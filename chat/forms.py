from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', required=True)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)
        return password

    def clean_username(self):
        username = self.cleaned_data['username']
        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            raise ValidationError('Пользователь с таким именем уже существует')
        return username
