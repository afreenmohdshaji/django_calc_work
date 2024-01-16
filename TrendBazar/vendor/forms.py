from django import forms
from api.models import Category

class LoginForm(forms.Form):
    username=forms.CharField(widget=(forms.TextInput)(attrs={"class":"form-control","placeholder":"Enter username"}))
    password=forms.CharField(widget=(forms.PasswordInput)(attrs={"class":"form-control","placeholder":"Enter Password"}))

class CategoryAddForm(forms.ModelForm):
    
    class Meta:
        model=Category
        exclude=("created_at","updated_at",)