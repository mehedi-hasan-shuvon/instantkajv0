from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User
from .forms import LoginForm, RegisterForm, RegisterFormModel

# Create your views here.
def index(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            #  check w/ data
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            exists = User.objects.filter(email=email, password=password).exists()
            if exists:
                return HttpResponseRedirect(reverse('success'))
            else:
                return HttpResponseRedirect(reverse('failure'))
    else:
        form = LoginForm()


    return  render(request,'authentication/index.html', {'form': form})


def success(request):
    return render(request, 'authentication/success.html')

def failure(request):
    return render(request, 'authentication/failure.html')

def register(request):

    form = RegisterForm()
    message = ""
    if request.method == "POST":
        # user sent data for registration
        form = RegisterForm(request.POST)

        if form.is_valid():
            # check data for duplicate
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            exists = User.objects.filter(email=email, password=password).exists()

            if not exists:
                User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
                message = "Account Created"

                # Reset Form
                form = RegisterForm()
            else:
                message = f"An account already exists with {email}"
        else:
            message = "Form not valid"
    else:
        form = RegisterForm()
        message = "Complete the form to register"

    
    return render(request, 'authentication/register.html', {'form': form, 'message': message})

# Bug exists
def register2(request):

    form = RegisterFormModel()
    message = ""
    if request.method == "POST":
        form = RegisterFormModel(request.POST)

        if form.is_valid():
            print("form valid")
            # check data for duplicate
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            exists = User.objects.filter(email=email, password=password).exists()

            if not exists:
                form.save()
                message = "Account Created"

                # Reset Form
                form = RegisterForm()
            else:
                message = f"An account already exists with {email}"
        else:
            print("form not valid")
            message = "Form not valid"
    else:
        form = RegisterFormModel()
        message = "Complete the form to register"

    return render(request, 'authentication/register2.html', {'form': form, 'message': message})