from django.db import models

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey('User',on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128,unique=True)
    price = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length = 128,primary_key=True)
    email = models.CharField(max_length = 128)
    fullName = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)

    def __str__(self):
        return self.name