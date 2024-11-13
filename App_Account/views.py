from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from App_Account.serializer import UserRegistrationSerializer

class UserRegistrationView(APIView):
    def post(self,request):
        form=UserRegistrationSerializer(data=request.data)
        if form.is_valid():
            form.save()
            return Response({'data':form.data,'status':status.HTTP_201_CREATED})
        return Response({'data':form.errors,'status':status.HTTP_400_BAD_REQUEST})
    
        
