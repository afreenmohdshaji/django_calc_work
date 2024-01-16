from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import UserSerializer


class RegisterationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        