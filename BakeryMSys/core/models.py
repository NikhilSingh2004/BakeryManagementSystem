from django.db import models

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=64)
    order_name = models.CharField(max_length=64)
    order_date = models.DateField(null=True)
    order_quantity = models.IntegerField()

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(null=False, max_length=128)
    password = models.CharField(null=False, max_length=256, default='')

