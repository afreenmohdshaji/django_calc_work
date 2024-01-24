"""
URL configuration for scrapboxapplication project.

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
from scrapboxapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.RegistrationView.as_view(),name="register"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('index/',views.IndexView.as_view(),name="index"),
    path('scrap/add/',views.ScrapAdd.as_view(),name='scrap-add'),
    path('profile/<int:pk>/update/',views.UserUpdateView.as_view(),name="profile-edit"), 
    path('profile/detail/<int:pk>/',views.UserProfileDetail.as_view(),name="profile-detail"),
    path('logout',views.LogOutView.as_view(),name="logout"),
    path('scrap/<int:pk>/detail/',views.ScrapDetailView.as_view(),name="scrap-detail"),
    path('scrap/<int:pk>/delete',views.ScrapDeleteView.as_view(),name="scrap-delete"),
    path('scrap/<int:pk>/update',views.ScrapEditView.as_view(),name="scrap-edit"),
    path('scrap/<int:pk>/wishlist',views.WishlistAddView.as_view(),name='wishlist'),
    path('scrap/wishlistview/',views.WishListView.as_view(),name="wishlistview"),
    path('scrap/myscraplist/',views.MyScrapListView.as_view(),name="myscrap-list")
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


