from django import forms

class RegisterForm(forms.Form):
    school_name = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()