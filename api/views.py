from django.shortcuts import render
from .serializer import DoctorSerializer
from .models import Doctor
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin





class DoctorgenericLC(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer   

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
     
    def put(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

    





class DonctorgenericRUD(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):

    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
     
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
     
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
    


     

    
