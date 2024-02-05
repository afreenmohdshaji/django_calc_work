from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from scrapboxapp.models import Scrap,UserProfile,Bids

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
    
        widgets={
                "username":forms.TextInput(attrs={
                    "class":"form-control",
                    "placeholder":"Enter username",
                    
                    }),
                "email":forms.EmailInput(attrs={
                    "class":"form-control",
                    "Placeholder":"Email"
                }),
        }
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder':"Enter a password",
            })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'Placeholder':'Confirm Password',
            })
        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

class LoginForm(forms.Form):
    username=forms.CharField(max_length=200,widget=(forms.TextInput)(attrs={"class":"form-control","placeholder":"Enter username"}))
    password=forms.CharField(max_length=200,widget=(forms.PasswordInput)(attrs={"class":"form-control","placeholder":"Enter password"}))

class ScrapForm(forms.ModelForm):
    class Meta:
        model=Scrap
        exclude=["user"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "condition":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "place":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "picture":forms.FileInput(attrs={"class":"form-control"}),
            "category":forms.Select(attrs={"class":"form-control"}),
            "status":forms.Select(attrs={"class":"form-control"}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=["user"]

class BidsForm(forms.ModelForm):
    class Meta:
        model= Bids
        fields=["amount"]
        widgets={
            "amount":forms.NumberInput(attrs={"class":"form-control"})
        }