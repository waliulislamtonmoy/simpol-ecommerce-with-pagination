from django.shortcuts import render

# Create your views here.


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Product,Order,OrderItem
from .serializer import ProductSerializer,OrderSerializer,OrderCreateSerializer

class userview(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user.username
        return Response(f"username is: {user}")
    
class ProductView(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
class OrderViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return OrderSerializer
    
    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order=serializer.save(user.request.user)
        order_serializer=OrderSerializer(order)
        return Response(order_serializer.data,status=status.HTTP_201_CREATED)            
        