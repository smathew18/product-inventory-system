# Generated by Django 2.2.6 on 2019-12-12 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('producttype', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('RESTOCKING', 'Item needs restocking in few days'), ('SOLD', 'Item already purchased')], default='AVAILABLE', max_length=20)),
                ('comments', models.CharField(default='No Issues', max_length=60)),
                ('quantity', models.IntegerField(default='50')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppliername', models.CharField(max_length=100)),
                ('supplieraddress', models.CharField(blank=True, max_length=100, null=True)),
                ('suppliercity', models.CharField(blank=True, max_length=20, null=True)),
                ('supplierstate', models.CharField(blank=True, max_length=20, null=True)),
                ('supplierzipcode', models.CharField(blank=True, max_length=10, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.IntegerField()),
                ('numberordered', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('productname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchaseorders', to='pis.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchaseorders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BillingOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billno', models.IntegerField()),
                ('billstatus', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billingorders', to='pis.PurchaseOrder')),
            ],
        ),
    ]
