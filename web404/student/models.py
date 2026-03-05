from django.db import models

# Create your models here.
class Product(models.Model):
    names=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    descripton=models.TextField()
    discount=models.IntegerField()
    # def __str__(self):
    #     return f"{self.names}  {self.price}"
class Staff(models.Model):
    full_name=models.CharField(max_length=200)
    gender=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    address=models.TextField()
    photo=models.ImageField(upload_to='photo/',default=None)
