from django import forms
from .models import contact,login

class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields = ["name","email","message"]
class loginform(forms.ModelForm):
    class Meta:
        model = login
        fields = ["email","password"]
