from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import EmployeSerializer,TaskSerializer
from api.models import Employee,Task
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import authentication,permissions

# Create your views here.

class EmployeeListViewSet(viewsets.ViewSet):

    def list(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        serializer=EmployeSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=EmployeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        serializer=EmployeSerializer(qs)
        return Response(data=serializer.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        emp_obj=Employee.objects.get(id=id)
        serializer=EmployeSerializer(data=request.data,instance=emp_obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employee.objects.get(id=id).delete()
        return Response(data={"messege":"deleted"})
    


    

class EmployeeModelViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAdminUser]
    authentication_classes=[authentication.TokenAuthentication]
    serializer_class=EmployeSerializer
    model=Employee
    queryset=Employee.objects.all()

    def list(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        if "department" in request.query_params:
            value=request.query_params.get("department")
            qs=qs.filter(department=value)
        serializer=EmployeSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    @action(methods=["get"],detail=False)
    def department(self,request,*args,**kwargs):
        data=Employee.objects.all().values_list("department",flat=True)
        return Response(data=data)
    
    
    @action(methods=["post"],detail=True)
    def add_task(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        emp_obj=Employee.objects.get(id=id)
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employees=emp_obj)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=["get"],detail=True)
    def tasks(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.filter(employees_id=id)
        serializer=TaskSerializer(qs,many=True)
        return Response(data=serializer.data)
    
class TaskView(viewsets.ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def update(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        task_obj=Task.objects.get(id=id)
        serializer=TaskSerializer(data=request.data,instance=task_obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        serializer=TaskSerializer(qs)
        return Response(data=serializer.data)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Task.objects.get(id=id).delete()
        return Response(data={"message":"task deleted"})
    
        