# Generated by Django 3.0 on 2020-04-12 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_income_incometype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incometype',
            name='name',
            field=models.CharField(choices=[('P', 'Property'), ('B', 'Business'), ('S', 'Salary'), ('O', 'Other')], default='Bank', max_length=2),
        ),
    ]