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


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ['id', 'name', 'email', 'password']


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Income
        fields = ['id', 'user_id', 'note', 'name', 'amount', 'timestamp']


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = ['id', 'user_id', 'note', 'name', 'amount', 'timestamp']


class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Saving
        fields = ['id', 'user_id', 'note', 'name', 'amount', 'timestamp', 'rate']


class IncomeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Income
        fields = ['id',  'name']


class SavingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SavingType
        fields = ['id', 'saving', 'name']


class ExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExpenseType
        fields = ['id', 'expense', 'name']


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Balance
        fields = ['id', 'user_id', 'status', 'amount']
