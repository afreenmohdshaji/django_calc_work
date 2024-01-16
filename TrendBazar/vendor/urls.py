from django.urls import path
from vendor import views

urlpatterns=[
    path("add",views.CategoryAddView.as_view(),name="category-add"),
    path("list",views.CategoryListView.as_view(),name="category-list"),
    path("<int:pk>/change",views.CategoryUpdateView.as_view(),name="category-update"),
]