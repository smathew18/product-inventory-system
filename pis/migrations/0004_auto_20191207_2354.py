# Generated by Django 2.2.6 on 2019-12-08 05:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pis', '0003_auto_20191207_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingorder',
            old_name='billdate',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='purchaseorderdate',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='billingorder',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('RESTOCKING', 'Item needs restocking in few days'), ('SOLD', 'Item already purchased')], default='AVAILABLE', max_length=20),
        ),
    ]
