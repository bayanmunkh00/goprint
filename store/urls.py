from django.urls import path

from .views import (
    OrderListView,
    ProductListView,
    JobsListView,
    create_product,
    create_order,
    create_jobs,
    )

urlpatterns = [
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('create-jobs/', create_jobs, name='create-jobs'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('jobs-list/', JobsListView.as_view(), name='jobs-list'),
    ]
