from django.shortcuts import render
from django.views.generic import View,FormView,CreateView,ListView,UpdateView
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from api.models import Category

from vendor.forms import LoginForm,CategoryAddForm
from vendor.decorators import login_required
# Create your views here.
dec=[login_required,never_cache]

class SigninView(FormView):
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
                print("Login successfully")
                return redirect("category-list")
        print("Failed to login")
        messages.error(request,"Password or username icorrect")
        return render(request,"login.html",{"form":form})

@method_decorator(dec,name="dispatch")
class CategoryAddView(CreateView):
    template_name="category_add.html"
    form_class=CategoryAddForm

    def get_success_url(self):
        return reverse("category-list")
    
@method_decorator(dec,name="dispatch")
class CategoryListView(ListView):
    template_name="category_list.html"
    model=Category
    context_object_name="data"

@method_decorator(dec,name="dispatch")
class CategoryUpdateView(UpdateView):
    template_name="category_update.html"
    form_class=CategoryAddForm
    model=Category

    def get_success_url(self):
        return reverse("category-list")

class SignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")