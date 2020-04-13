from django.shortcuts import render
from cms import serializers
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from cms import serializers, models
from rest_framework import filters, pagination
from rest_framework.decorators import api_view
from rest_framework.response import Response


# framework
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# custom models
@api_view(['POST',])
def reg_view(request):
    serializer = serializers.UserRegisterSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        client = serializer.save()
        data['response'] = 'Success'
        data['email'] = client.email
        data['username'] = client.username
    else:
        data = serializer.error
        return Response(data)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination.PageNumberPagination.page_size_query_param = 'page_size'


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = models.Income.objects.all()
    serializer_class = serializers.IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination.PageNumberPagination.page_size_query_param = 'page_size'


class SavingViewSet(viewsets.ModelViewSet):
    queryset = models.Saving.objects.all()
    serializer_class = serializers.SavingSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination.PageNumberPagination.page_size_query_param = 'page_size'


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination.PageNumberPagination.page_size_query_param = 'page_size'


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = models.Balance.objects.all()
    serializer_class = serializers.BalanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination.PageNumberPagination.page_size_query_param = 'page_size'


class ExpenseTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ExpenseType.objects.all()
    serializer_class = serializers.ExpenseTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination.PageNumberPagination.page_size_query_param = 'page_size'


class IncomeTypeViewSet(viewsets.ModelViewSet):
    queryset = models.IncomeType.objects.all()
    serializer_class = serializers.IncomeTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination.PageNumberPagination.page_size_query_param = 'page_size'


class SavingTypeViewSet(viewsets.ModelViewSet):
    queryset = models.SavingType.objects.all()
    serializer_class = serializers.SavingTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination.PageNumberPagination.page_size_query_param = 'page_size'
