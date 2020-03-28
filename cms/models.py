from django.db import models


# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    details = models.JSONField(default=dict)
    ex_points = models.DecimalField(max_digits=100, decimal_places=3, default=0)

    class Meta:
        ordering = ['id']


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    details = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=100, decimal_places=3, default=0)
    discount_rate = models.DecimalField(max_digits=100, decimal_places=3, default=0)
    quantity = models.ForeignKey("Store", on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['id']


class Store(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey("Products", on_delete=models.CASCADE, null=True, )
    quantity = models.DecimalField(max_digits=100, decimal_places=3, default=0)
    purchase_rate = models.DecimalField(max_digits=100, decimal_places=3, default=0)

    class Meta:
        ordering = ['id']


class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey("Customer", on_delete=models.CASCADE, null=True)
    details = models.JSONField(default=dict)
    expenses = models.DecimalField(max_digits=100, decimal_places=3, default=0)
    product_id = models.ForeignKeyManyToManyField(Products, related_name='product')
    quantity = models.ForeignKeyManyToManyField(Store, related_name='quantity')

    class Meta:
        ordering = ['id']
