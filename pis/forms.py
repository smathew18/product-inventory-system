from django import forms
from django.contrib.auth.models import User

from .models import Product,Supplier,PurchaseOrder,BillingOrder

class ProductForm(forms.ModelForm):
   class Meta:
       model = Product
       fields = ('productname', 'producttype', 'price', 'status', 'comments', 'quantity' )


class SupplierForm(forms.ModelForm):
   class Meta:
       model = Supplier
       fields = ('suppliername', 'supplieraddress', 'suppliercity', 'supplierstate', 'supplierzipcode' )

class PurchaseOrderForm(forms.ModelForm):
   class Meta:
       model = PurchaseOrder
       fields = ('user','orderId', 'productname', 'numberordered')


class BillingOrderForm(forms.ModelForm):
   class Meta:
       model = BillingOrder
       fields = ('orderId', 'billno', 'billstatus')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
