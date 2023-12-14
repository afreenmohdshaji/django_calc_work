from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,FormView,CreateView,UpdateView,DetailView
from socialapp.forms import RegistrationForm,LoginForm,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from socialapp.models import UserProfile

from django.urls import reverse,reverse_lazy
# Create your views here.


class SignUpView(CreateView):
    # def get(self,request,*args,**kwargs):
    #     form=RegistrationForm()
    #     return render(request,"register.html",{"form":form})
    template_name="register.html"
    form_class=RegistrationForm

    def get_success_url(self):
        return reverse("signin")

    # def post(self, request,*args,**kwargs):
    #     form=RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("register.html")
    #     else:
    #         return render(request,"register.html",{"form":form})
        
class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=uname,password=pwd)
            if user_obj:
                login(request,user_obj)
                return redirect("index")
        return render(request,"login.html",{"form":form})
    
class IndexView(TemplateView):
    template_name="index.html"


class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    

class ProfileUpdateView(UpdateView):
    model = UserProfile
    template_name = "profile_edit.html"
    form_class = UserProfileForm

    def form_valid(self, form):
        print("Form is valid.")
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("index")

    

    
class ProfileDetailView(DetailView):
    template_name="profile.html"
    model=UserProfile
    context_object_name="data"