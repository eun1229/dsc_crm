from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import CustomUserCreationForm

# Create your views here.

def index(request):
  return render(request, 'crm_app/index.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user and profile
            login(request, user)  # Log the user in after registration
            return redirect('index')  # Redirect to a home page or dashboard
    else:
        form = CustomUserCreationForm()

    return render(request, 'crm_app/register.html', {'form': form})
