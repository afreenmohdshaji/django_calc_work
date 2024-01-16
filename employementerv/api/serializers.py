from rest_framework import serializers
from api.models import Employee,Task




class TaskSerializer(serializers.ModelSerializer):
    employees=serializers.StringRelatedField()
    class Meta:
        model=Task
        fields="__all__"
        read_only_fields=["id","employees","assg_date"]

class EmployeSerializer(serializers.ModelSerializer):
    tasks=TaskSerializer(read_only=True,many=True)
    class Meta:
        model=Employee
        fields="__all__"
        read_only_fields=["id"]
        