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


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id',  'name', 'email', 'password']
