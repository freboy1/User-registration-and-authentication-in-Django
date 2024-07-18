from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Create your views here.
def home_view(request):
    return render(request, 'crm/home.html')

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'crm/register.html', context)


def dashboard(request):
    return render(request, 'crm/dashboard.html')