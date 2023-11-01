"""
URL configuration for calculatorapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("helloworld/",views.HelloworldView.as_view()),
    path("morning/",views.GoodmorningView.as_view()),
    path("add/",views.AdditionView.as_view(),name="add"),
    path("sub/",views.SubtractionView.as_view(),name="sub"),
    path("div/",views.DivisionView.as_view(),name="div"),
    path("mul/",views.MultiplicatonView.as_view(),name="mul"),
    path("cube/",views.CubeView.as_view(),name="cube"),
    path("fact/",views.FactorialView.as_view(),name="fact"),
    path("leap/",views.LeapYearView.as_view(),name="leapyear"),
    path("bmi/",views.BmiView.as_view(),name="bmi_cal"),
    path("",views.IndexView.as_view()),
]
