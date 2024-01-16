from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken



rounter=DefaultRouter()
rounter.register('v1/employee',views.EmployeeListViewSet,basename="employee")
rounter.register('v2/employee',views.EmployeeModelViewSet,basename="employe")
rounter.register('v2/task',views.TaskView,basename="task")

urlpatterns=[
    path('v2/token/',ObtainAuthToken.as_view()),

]+ rounter.urls