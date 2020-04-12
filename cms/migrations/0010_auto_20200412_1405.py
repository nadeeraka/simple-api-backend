# Generated by Django 3.0 on 2020-04-12 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_auto_20200412_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('S', 'Salary'), ('P', 'Property'), ('B', 'Business'), ('O', 'Other')], default='Bank', max_length=2)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='savingtype',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='income',
            name='name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='cms.IncomeType'),
        ),
    ]