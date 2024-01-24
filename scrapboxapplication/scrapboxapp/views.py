from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,ListView,TemplateView,UpdateView,DetailView,DeleteView
from scrapboxapp.forms import RegistrationForm,LoginForm,ScrapForm,UserProfileForm
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from scrapboxapp.models import Scrap,UserProfile,WishList
from django.views.decorators.cache import never_cache 
from scrapboxapp.decorators import login_required
from django.utils.decorators import method_decorator 


decs=[login_required,never_cache]



class RegistrationView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm

    def get_success_url(self):
        return reverse("login")

class LoginView(FormView):
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
            else:
                messages.error(self.request, 'Invalid username or password')
        return render(request,"login.html",{"form":form})

@method_decorator(decs,name="dispatch")
class IndexView(ListView):
    model=Scrap
    template_name="index.html"
    context_object_name = 'data'

    

# class ScrapListView(View):
#     def get(self,request,*args,**kwargs):
#         qs=Scrap.objects.all()
#         return render(request,"index.html",{"data":qs})

@method_decorator(decs,name="dispatch")
class ScrapAdd(CreateView):
    form_class=ScrapForm
    template_name="scrapadd.html"

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("index")    

@method_decorator(decs,name="dispatch")
class UserUpdateView(UpdateView):
    model=UserProfile
    form_class=UserProfileForm
    template_name="profile_edit.html"
    
    

    def get_success_url(self):
        return reverse("index")

@method_decorator(decs,name="dispatch")   
class UserProfileDetail(DetailView):
    model=UserProfile
    template_name="profile_detail.html"
    context_object_name="data"
    
@method_decorator(decs,name="dispatch")
class LogOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")

@method_decorator(decs,name="dispatch")
class ScrapDetailView(DetailView):
    model=Scrap
    template_name="scrap-detail.html"
    context_object_name="data"
    
@method_decorator(decs,name="dispatch")
class ScrapDeleteView(DeleteView):
    model = Scrap
    template_name = 'myscraplist.html'
    success_url = reverse_lazy('index')

@method_decorator(decs,name="dispatch")
class ScrapEditView(UpdateView):
    model=Scrap
    form_class=ScrapForm
    template_name="scrap_edit.html"
    
    def get_success_url(self):
        return reverse("scrap-detail",kwargs={'pk': self.object.pk})

@method_decorator(decs,name="dispatch")    
class WishlistAddView(View):
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        scrap_obj=Scrap.objects.get(id=id)
        print(scrap_obj)
        action=request.POST.get("action")

        wishlist, created = WishList.objects.get_or_create(user=request.user)
        if action == "add":
            wishlist.scrap.add(scrap_obj)
        elif action == "remove":
            wishlist.scrap.remove(scrap_obj)
            print("removed")
        elif action == "remove_from_wish":
            wishlist.scrap.remove(scrap_obj)
            return redirect("wishlistview")
        return redirect("index")
    
    

@method_decorator(decs,name="dispatch")
class WishListView(View):

    def get(self,request,*args,**kwargs):
        qs=WishList.objects.get(user_id=request.user.id)
        wishitems=Scrap.objects.exclude(user=request.user)
        return render(request,"wishlist.html",{"data":qs,"items":wishitems})


class MyScrapListView(View):
    def get(self,request,*args,**kwargs):
        qs=Scrap.objects.filter(user_id=request.user.id)
        return render(request,"myscraplist.html",{"data":qs})
    
    




