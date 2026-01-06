from django.db import models
from users.models import *;
from products.models import *;
# Create your models here.
class Order(models.Model):
    ststu=(
        ('created','CREATED'),
        ('paid','PAID'),
        ('shipped','SHIPPED'),
        ('delivered','DELIVERED'),
    )
    id=models.AutoField(primary_key=True)
    customer_id=models.ForeignKey(UsersData,on_delete=models.CASCADE)
    address_id=models.ForeignKey(addresses,on_delete=models.CASCADE)
    total_amount=models.IntegerField()
    status=models.CharField(max_length=20,choices=ststu,default="created")
    created_at=models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quntity=models.IntegerField()
    price=models.IntegerField()

