from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

Inventory={
    ('AVAILABLE','Item ready to be purchased'),
    ('SOLD','Item already purchased'),
    ('RESTOCKING','Item needs restocking in few days')
}
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products',null=True)
    productname = models.CharField(max_length=100)
    producttype = models.CharField(max_length=100,blank=False)
    price = models.IntegerField()
    status = models.CharField(max_length=20,choices=Inventory,default='AVAILABLE')
    comments = models.CharField(max_length=60,default="No Issues")
    quantity = models.IntegerField(blank=False, null=False,default="50")
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.productname)

class Supplier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suppliers',null=True)
    #product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='suppliers')
    suppliername = models.CharField(max_length=100)
    supplieraddress = models.CharField(max_length=100,blank=True, null=True)
    suppliercity = models.CharField(max_length=20,blank=True, null=True)
    supplierstate = models.CharField(max_length=20,blank=True, null=True)
    supplierzipcode = models.CharField(max_length=10,blank=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.suppliername)

class PurchaseOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchaseorders')
    orderId = models.IntegerField()
    productname = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchaseorders')
    # suppliername = models.ForeignKey(Supplier,on_delete=models.CASCADE, related_name='purchaseorders')
   #  purchaseorderdate = models.DateTimeField(default=timezone.now)
    numberordered = models.IntegerField()
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.orderId)


class BillingOrder(models.Model):
    orderId = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='billingorders')
    billno = models.IntegerField()
    # billdate = models.DateTimeField(default=timezone.now)
    billstatus = models.CharField(max_length=50,blank=True,null=True);
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.billno)


