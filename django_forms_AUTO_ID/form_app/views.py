from django.shortcuts import render
from .forms import RegisterForm

def register(request):
    form = RegisterForm(auto_id='Onkar_%s', label_suffix=' -- ', initial={'name': 'Onkar Nardekar', 'email': 'username@gmail.com'})
    context = {'form': form}
    return render(request, 'form_app/register.html', context)