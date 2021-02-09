from django import forms

from . import models

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30, label="Email")
    password = forms.CharField(max_length=15, widget=forms.PasswordInput, label="Password")

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=12, widget=forms.PasswordInput)

class RegisterFormModel(forms.ModelForm):

    class Meta:
        model = models.User
        fields = '__all__'
        # exclude = []
        widgets = {
            'password': forms.PasswordInput(),
        }