from django.contrib import admin
from .models import *

# Register your models here.

class ProductList(admin.ModelAdmin):
    list_display = ( 'productname', 'producttype', 'status' )
    list_filter = ( 'productname', 'producttype')
    search_fields = ('productname', )
    ordering = ['productname']


class SupplierList(admin.ModelAdmin):
    list_display = ( 'suppliername', 'supplieraddress')
    list_filter = ( 'suppliername','supplieraddress')
    search_fields = ('suppliername', )
    ordering = ['suppliername']

class PurchaseOrderList(admin.ModelAdmin):
    list_display = ( 'productname', 'purchaseorderdate','numberordered')
    list_filter = ( 'productname', 'numberordered')
    search_fields = ('productname', )
    ordering = ['purchaseorderdate']

class BillingOrderList(admin.ModelAdmin):
    list_display = ( 'billdate','billno')
    list_filter = ( 'billno','billstatus')
    search_fields = ( 'billno', )
    ordering = ['billno']


admin.site.register(Product, ProductList)
admin.site.register(Supplier, SupplierList)
admin.site.register(PurchaseOrder, PurchaseOrderList)
admin.site.register(BillingOrder,BillingOrderList)
