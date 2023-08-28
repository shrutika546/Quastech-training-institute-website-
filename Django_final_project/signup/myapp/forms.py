from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import user_model
class user_form(forms.ModelForm):
    class Meta:
        model=user_model
        fields="__all__"

class signupform(UserCreationForm):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    email=forms.CharField(max_length=50)

    class Meta:
        model=User
        fields=('username','password1','password2','email','first_name','last_name')

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)