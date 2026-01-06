from django.db import models

# Create your models here.
class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    descripation=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    


