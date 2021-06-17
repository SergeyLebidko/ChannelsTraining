from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', required=True)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)