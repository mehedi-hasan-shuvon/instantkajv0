from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User
from .forms import LoginForm

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
    return render(request, 'authentication/register.html')