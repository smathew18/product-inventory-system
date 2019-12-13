from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *
from django.shortcuts import render


# Create your views here.


now = timezone.now()
def home(request):
   return render(request, 'pis/home.html',
                 {'pis': home})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'pis/register_done.html', {'new_user': new_user})
    else:
      user_form = UserRegistrationForm()
      return render(request, 'pis/register.html', {'user_form': user_form})

@login_required
def purchaseorder_list(request):
    purchaseorders = PurchaseOrder.objects.filter(created_date__lte=timezone.now())
    return render(request, 'pis/purchaseorder_list.html', {'purchaseorders': purchaseorders})


@login_required
def purchaseorder_new(request):
    if request.method == "POST":
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            purchaseorder = form.save(commit=False)
            purchaseorder.created_date = timezone.now()
            purchaseorder.save()
            purchaseorders = PurchaseOrder.objects.filter(created_date__lte=timezone.now())
            return render(request, 'pis/purchaseorder_list.html',
                          {'purchaseorders': purchaseorders})
    else:
        form = PurchaseOrderForm()
    return render(request, 'pis/purchaseorder_new.html', {'form': form})


@login_required
def purchaseorder_edit(request, pk):
    purchaseorder = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method == "POST":
        form = PurchaseOrderForm(request.POST, instance=purchaseorder)
        if form.is_valid():
            purchaseorder = form.save()
            purchaseorder.updated_date = timezone.now()
            purchaseorder.save()
            purchaseorders = PurchaseOrder.objects.filter(created_date__lte=timezone.now())
            return render(request, 'pis/purchaseorder_list.html', {'purchaseorders': purchaseorders})
    else:
        form = PurchaseOrderForm(instance=purchaseorder)
    return render(request, 'pis/purchaseorder_edit.html', {'form': form})


@login_required
def purchaseorder_delete(request, pk):
    purchaseorder = get_object_or_404(PurchaseOrder, pk=pk)
    purchaseorder.delete()
    return redirect('pis:purchaseorder_list')


@login_required
def billingorder_list(request):
    billingorders = BillingOrder.objects.filter(created_date__lte=timezone.now())
    return render(request, 'pis/billingorder_list.html', {'billingorders': billingorders})


@login_required
def billingorder_new(request):
    if request.method == "POST":
        form = BillingOrderForm(request.POST)
        if form.is_valid():
            billingorder = form.save(commit=False)
            billingorder.created_date = timezone.now()
            billingorder.save()
            billingorders = BillingOrder.objects.filter(created_date__lte=timezone.now())
            return render(request, 'pis/billingorder_list.html',
                          {'billingorders': billingorders})
    else:
        form = BillingOrderForm()
    return render(request, 'pis/billingorder_new.html', {'form': form})


@login_required
def billingorder_edit(request, pk):
    billingorder = get_object_or_404(BillingOrder, pk=pk)
    if request.method == "POST":
        form = BillingOrderForm(request.POST, instance=billingorder)
        if form.is_valid():
            billingorder = form.save()
            billingorder.updated_date = timezone.now()
            billingorder.save()
            billingorders = BillingOrder.objects.filter(created_date__lte=timezone.now())
            return render(request, 'pis/billingorder_list.html', {'billingorders': billingorders})
    else:
        form = BillingOrderForm(instance=billingorder)
    return render(request, 'pis/billingorder_edit.html', {'form': form})


@login_required
def billingorder_delete(request, pk):
    billingorder = get_object_or_404(BillingOrder, pk=pk)
    billingorder.delete()
    return redirect('pis:billingorder_list')


@login_required
def supplier_list(request):
    suppliers = Supplier.objects.filter(created_date__lte=timezone.now())
    return render(request, 'pis/supplier_list.html', {'suppliers': suppliers})


@login_required
def supplier_new(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.created_date = timezone.now()
            supplier.save()
            suppliers = Supplier.objects.filter(created_date__lte=timezone.now())
            return render(request, 'pis/supplier_list.html',
                          {'suppliers': suppliers})
    else:
        form = SupplierForm()
    return render(request, 'pis/supplier_new.html', {'form': form})


@login_required
def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            supplier = form.save()
            supplier.updated_date = timezone.now()
            supplier.save()
            suppliers = Supplier.objects.filter(created_date__lte=timezone.now())
            return render(request, 'pis/supplier_list.html', {'suppliers': suppliers})
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'pis/supplier_edit.html', {'form': form})


@login_required
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    supplier.delete()
    return redirect('pis:supplier_list')


@login_required
def product_list(request):
    products = Product.objects.filter(created_date__lte=timezone.now())
    return render(request, 'pis/product_list.html', {'products': products})


@login_required
def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_date = timezone.now()
            product.save()
            products = Product.objects.filter(created_date__lte=timezone.now())
            return render(request, 'pis/product_list.html',
                          {'products': products})
    else:
        form = ProductForm()
        # print("Else")
    return render(request, 'pis/product_new.html', {'form': form})


@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            product.updated_date = timezone.now()
            product.save()
            products = Product.objects.filter(created_date__lte=timezone.now())
            return render(request, 'pis/product_list.html', {'products': products})
    else:
        # print("else")
        form = ProductForm(instance=product)
    return render(request, 'pis/product_edit.html', {'form': form})


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('pis:product_list')



