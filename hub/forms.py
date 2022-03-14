from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentForm(forms.Form):
    first_name = forms.CharField(
        label='Prenom'
    )
    last_name = forms.CharField(
        label='Nom'
    )
    email = forms.EmailField(
        label='email',

    )
class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__" #['last_name',first_name','email']
class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username', 'first_name', 'last_name', 'email')
