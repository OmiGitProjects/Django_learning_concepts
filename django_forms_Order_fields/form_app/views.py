from django.shortcuts import render
from .forms import RegisterForm

def registerForm(request):
    form = RegisterForm(initial={'school_name': 'Mahindra Academy'})
    form.order_fields(field_order=['first_name', 'last_name', 'school_name'])
    context = {'form': form}
    return render(request, 'form_app/register.html', context)