from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User, Group
from cms import models


# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id', 'code', 'name', 'email', 'details', 'ex_points']


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = ['id', 'code', 'name', 'name', 'details', 'price', 'discount_rate', 'quantity']


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Store
        fields = ['id', 'product_id', 'quantity', 'purchase_rate']


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Purchase
        fields = ['id', 'customer_id', 'details', 'expenses', 'product_id', 'quantity']
