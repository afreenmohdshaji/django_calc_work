from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserModel
from todoapp.models import Todoos


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        widgets={
                "username":forms.TextInput(attrs={"class":"form-control"}),
                "email":forms.TextInput(attrs={"class":"form-control"}),
                "password1":forms.TextInput(attrs={"class":"form-control"}),
                "password2":forms.TextInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={"class":"form-control"}))


class TodoForm(forms.ModelForm):
    class Meta:
        model=Todoos
        fields=["name"]
        