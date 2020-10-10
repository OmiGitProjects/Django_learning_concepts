from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(initial='John', help_text='Only 30 Characters')
    last_name = forms.CharField()
    school_name = forms.CharField()