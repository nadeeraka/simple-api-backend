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
    INCOME_CHOICES = [
        ('S', 'Salary'),
        ('P', 'Property'),
        ('B', 'Business'),
        ('O', 'Other')
    ]

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=1, default='Salary', choices=INCOME_CHOICES)
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['id']


class Expense(models.Model):
    EXPENSE_CHOICES = [
        ('L', 'Lifestyle'),
        ('E', 'Entertainment'),
        ('D', 'Donation'),
        ('ED', 'Eduction'),
        ('O', 'Other'),
        ('F', 'Fixed'),
        ('EQ', 'Equipment'),
        ('M', 'Mortgage'),
        ('F', 'Foods'),
        ('H', 'Health'),

    ]

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=2, default='Salary', choices=EXPENSE_CHOICES)
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['id']


class Saving(models.Model):
    EXPENSE_CHOICES = [
        ('L', 'Lifestyle'),
        ('E', 'Entertainment'),
        ('D', 'Donation'),
        ('ED', 'Eduction'),
        ('O', 'Other'),
        ('F', 'Fixed'),
        ('EQ', 'Equipment'),

    ]

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True)
    type = models.ForeignKey('SavingType', on_delete=models.CASCADE, related_name="savings")
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    rate = models.DecimalField(max_digits=100, decimal_places=4, default=0)

    class Meta:
        ordering = ['id']


class Balance(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)

    class Meta:
        ordering = ['id']
