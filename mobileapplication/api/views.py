from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from mobile.models import Mobiles
from api.serializers import MobilesSerializers
from rest_framework import viewsets

class MobileListCreateView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        serializer=MobilesSerializers(qs,many=True)
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer=MobilesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
class MobileUpdateDetailDestroyView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Mobiles.objects.get(id=id)
        serializer=MobilesSerializers(qs)
        return Response(data=serializer.data)
    
    def put(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        mob_obj=Mobiles.objects.get(id=id)
        serializer=MobilesSerializers(data=request.data,instance=mob_obj)
        if serializer.is_valid():
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Mobiles.objects.get(id=id).delete()
        return Response(data={"message":"mobile deleted"})
    


class MobileViewSetView(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        serializer=MobilesSerializers(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Mobiles.objects.get(id=id)
        serializer=MobilesSerializers(qs)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=MobilesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        mob_obj=Mobiles.objects.get(id=id)
        serializer=MobilesSerializers(data=request.data,instance=mob_obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Mobiles.objects.get(id=id).delete()
        return Response(data={"message":"deleted"})
    

        