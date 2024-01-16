from rest_framework import serializers
from django.contrib.auth.models import User
from todoapp.models import Todoos

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todoos
        fields="__all__"
        read_only_fields=["status","id","user"]