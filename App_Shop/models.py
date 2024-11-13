from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name=models.CharField( max_length=150)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='orders')
    total_price=models.DecimalField( max_digits=5, decimal_places=2,default=0.00)
    created_at=models.DateTimeField( auto_now=False )
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField( max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name} in order {self.price}"