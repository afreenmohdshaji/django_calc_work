from django import forms

from mobile.models import Mobiles

from django.contrib.auth.models import User

class Mobilesform(forms.ModelForm):
    class Meta:
        model=Mobiles
        fields="__all__"

        widgets={
                "name":forms.TextInput(attrs={"class":"form-control"}),
                "price":forms.NumberInput(attrs={"class":"form-control"}),
                "brand":forms.TextInput(attrs={"class":"form-control"}),
                "specs":forms.TextInput(attrs={"class":"form-control"}),
                "display":forms.TextInput(attrs={"class":"form-control"})
                
        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]

        widgets={
                "username":forms.TextInput(attrs={"class":"form-control"}),
                "email":forms.TextInput(attrs={"class":"form-control"}),
                "password":forms.PasswordInput(attrs={"class":"form-control"})

        }

class LoginForm(forms.Form):
    username=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={"class":"form-control"}))
   

