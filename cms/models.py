from datetime import datetime

from django.db import models


# Create your models here.


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['id']


class Income(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True)
    type = models.ForeignKey('IncomeType', on_delete=models.CASCADE, related_name="incomes")
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['id']


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True)
    type = models.ForeignKey("ExpenseType", on_delete=models.CASCADE, related_name="expenses")
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['id']


class Saving(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True)
    type = models.ForeignKey('SavingType', on_delete=models.CASCADE, related_name="savings")
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    rate = models.DecimalField(max_digits=100, decimal_places=4, default=0)

    class Meta:
        ordering = ['id']


class IncomeType(models.Model):
    id = models.AutoField(primary_key=True)
    income = models.ForeignKey(Income, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['id']


class ExpenseType(models.Model):
    id = models.AutoField(primary_key=True)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['id']


class SavingType(models.Model):
    id = models.AutoField(primary_key=True)
    saving = models.ForeignKey(Saving, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['id']


class Balance(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)

    class Meta:
        ordering = ['id']
