from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home_view(request):
    return render(request, 'crm/home.html')

def register(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'crm/register.html', context)