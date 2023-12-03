from django.shortcuts import render,redirect
from django.views.generic import View
from todoapp.forms import UserForm,LoginForm,TodoForm
from django.contrib.auth import authenticate,login,logout
from todoapp.models import Todoos
from django.utils.decorators import method_decorator

# Create your views here.

def sighin_requred(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
        
    return wrapper

def owner_permision_requred(fn):
    def wrapper(request,*args,**kwargs):
        id=kwargs.get("pk")
        todo_object=Todoos.objects.get(id=id)
        if todo_object.user!=request.user:
            logout(request)
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

decs=[sighin_requred,owner_permision_requred]
class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=UserForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            print("account created")
            return redirect("login")
        else:
            return render(request,"registration.html",{"form":form})
        

class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=uname,password=pwd)
            if user_obj:
                login(request,user_obj)
                return redirect("index")
        print("invalid")
        return render(request,"login.html",{"form":form})

@method_decorator(sighin_requred,name="dispatch")
class IndexView(View):
    def get(self,request,*args,**kwargs):
        form=TodoForm()
        qs=Todoos.objects.filter(user=request.user)
        pending_count=Todoos.objects.filter(status="todo",user=request.user).count()
        in_progress_count=Todoos.objects.filter(status="inprogress",user=request.user).count()
        finished_count=Todoos.objects.filter(status="completed",user=request.user).count

        return render(request,"index.html",{"form":form,
                                            "data":qs,
                                            "pending":pending_count,
                                            "in_progress":in_progress_count,
                                            "finished":finished_count
                                            })
    def post(self,request,*args,**kwargs):
        form=TodoForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return redirect("index")
        else:
            return render(request,"index.html",{"form":form})

@method_decorator(decs,name="dispatch")
class UpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        if "status" in request.GET:
            value=request.GET.get("status")
            if value=="inprogress":
                Todoos.objects.filter(id=id).update(status="inprogress")
            elif value=="completed":
                Todoos.objects.filter(id=id).update(status="completed")
        return redirect("index")

@method_decorator(decs,name="dispatch")   
class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todoos.objects.filter(id=id).delete()
        return redirect("index")
        
@method_decorator(sighin_requred,name="dispatch")
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")