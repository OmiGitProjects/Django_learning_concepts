from django.shortcuts import render
from .forms import StudentRegistration

def showform_data(request):
    form = StudentRegistration()
    context = {'form': form}
    return render(request, 'student_info/registration.html', context)