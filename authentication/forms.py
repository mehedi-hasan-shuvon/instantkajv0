from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30)
    password = forms.CharField(max_length=15)

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    