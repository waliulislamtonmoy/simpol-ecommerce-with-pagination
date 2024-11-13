from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Product,Order,OrderItem

class ProductSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','price']
        
class OrderItemSerializer(ModelSerializer):
    orders=ProductSerializer(read_only=True)
    class Meta:
        model=OrderItem
        fields=['product','quantity','price']

class OrderSerializer(ModelSerializer):
    items=OrderItemSerializer(many=True,read_only=True)
    class Meta:
        model=Order
        fields=['id','total_price','created_at','items']
        read_only_fields=['user','totla_price','created_at']
        
class OrderCreateSerializer(serializers.Serializer):
    products=serializers.ListField(
        child=serializers.DictField(child=serializers.IntegerField())
    )
    
    def create(self,validate_data):
        user=self.context['request'].user
        products_data=validate_data.pop('products')
        order=Order.objects.create(user=user)
        total_price=0
        for item in products_data:
            product_id=item.get('product.id')
            quantity=item.get('quantity')
            product=Product.objects.get(id=product_id)
            price=product.price*quantity
            
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price
            )
            total_price+=price 
            order.total_price=total_price
            order.save()
            return order
            
            