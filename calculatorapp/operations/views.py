from django.shortcuts import render

# Create your views here.
from django.views.generic import View

class HelloworldView(View):
    def get(self,request,*args ,**kwargs):
        print("inside hello world view")
        return render(request,"helloworld.html")

class GoodmorningView(View):
    def get(self,request,*args ,**kwargs):
        return render(request,"gm.html")
    

class AdditionView(View):
    def get(self,request,*args ,**kwargs):
        return render(request,"add.html")
    def post(self,request,*args ,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print(result)
        return render(request,"add.html",{"output":result})
    
class SubtractionView(View):
    def get(self,request,*args ,**kwargs):
        return render(request,"sub.html")
    def post(self,request,*args ,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)-int(n2)
        print(result)
        return render(request,"sub.html",{"output":result})
    
class DivisionView(View):
    def get(self,request,*args ,**kwargs):
        return render(request,"div.html")
    def post(self,request,*args ,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)/int(n2)
        print(result)
        return render(request,"div.html",{"output":result})
    
class MultiplicatonView(View):
    def get(self,request,*args ,**kwargs):
        return render(request,"mul.html")
    def post(self,request,*args ,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)*int(n2)
        print(result)
        return render(request,"mul.html",{"output":result})
    
class CubeView(View):
    def get(self,request,*args ,**kwargs):
        return render(request,"cube.html")
    def post(self,request,*args ,**kwargs):
        n1=request.POST.get("num1")
        
        result=int(n1)**3
        print(result)
        return render(request,"cube.html",{"output":result})
    
class FactorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"fact.html")
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")

        fact=1
        
        for i in range(1,int(n)+1):
            fact=fact*i
        print(fact)
        return render(request,"fact.html",{"output":fact})
    
class LeapYearView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"lp.html")
    
    def post(self,request,*args,**kwargs):
        year=int(request.POST.get("year"))

        if(year %100==0 and year %400==0 or year %100!=0 and year %4==0):
            result=f"{year} is leap year"
        else:
            result=f"{year} is not leap year"

            return render(request,"lp.html",{"out":result})
        
class BmiView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"bmi.html")
    def post(self,request,*args,**kwargs):
        num1=int(request.POST.get("kg"))
        num2=int(request.POST.get("cm"))

        bmi=int(num1/(num2)**2)

        return render(request,"bmi.html",{"out":bmi})

    

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")