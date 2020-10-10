from django.shortcuts import render
from .forms import RegisterForm

def registerForm(request):
    form = RegisterForm(initial={'school_name': 'Mahindra Academy'})
    context = {'form': form}
    return render(request, 'form_app/register.html', context)