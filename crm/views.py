from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home_view(request):
    return render(request, 'crm/home.html')

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            return redirect('home')

    context = {'form': form}
    return render(request, 'crm/register.html', context)