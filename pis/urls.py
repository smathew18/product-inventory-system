
from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = 'pis'
urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^register/$', views.register, name='register'),
    # change password urls
    path('password_change/',
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('pis:password_change_done')),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('pis:password_reset_done')),
         {'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('pis:password_reset_complete')),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('product_list', views.product_list, name='product_list'),
    path('product/create/', views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('supplier_list', views.supplier_list, name='supplier_list'),
    path('supplier/create/', views.supplier_new, name='supplier_new'),
    path('supplier/<int:pk>/edit/', views.supplier_edit, name='supplier_edit'),
    path('supplier/<int:pk>/delete/', views.supplier_delete, name='supplier_delete'),
    path('purchaseorder_list', views.purchaseorder_list, name='purchaseorder_list'),
    path('purchaseorder/create/', views.purchaseorder_new, name='purchaseorder_new'),
    path('purchaseorder/<int:pk>/edit/', views.purchaseorder_edit, name='purchaseorder_edit'),
    path('purchaseorder/<int:pk>/delete/', views.purchaseorder_delete, name='purchaseorder_delete'),
    path('billingorder_list', views.billingorder_list, name='billingorder_list'),
    path('billingorder/create/', views.billingorder_new, name='billingorder_new'),
    path('billingorder/<int:pk>/edit/', views.billingorder_edit, name='billingorder_edit'),
    path('billingorder/<int:pk>/delete/', views.billingorder_delete, name='billingorder_delete'),

]
