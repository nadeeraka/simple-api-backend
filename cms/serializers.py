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


# custome serializr

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ['id', 'name', 'email']


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Income
        fields = ['user_id', 'note', 'name', 'amount', ]


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = ['user_id', 'note', 'name', 'amount', ]


class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Saving
        fields = ['user_id', 'note', 'name', 'amount', 'timestamp', 'rate']


class IncomeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Income
        fields = ['name']


class SavingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SavingType
        fields = ['name']


class ExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExpenseType
        fields = ['name']


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Balance
        fields = ['id', 'user_id', 'status', 'amount']


# auth

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ['email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # def save(self):
    #     client = models.Client(
    #         email=self.validated_data['email'],
    #         username=self.validated_data['username']
    #     )
    #     password = self.validated_data['password']
    #     password2 = self.validated_data['password2']
    #
    #     if password != password2:
    #         return serializers.ValidationError({'password': 'Password match'})
    #     models.Client.set_password(password)
    #     client.save()
    #     return client
