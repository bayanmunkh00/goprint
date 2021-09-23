from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import (
    Product,
    Order,
    Jobs
    )
from .forms import (
    ProductForm,
    OrderForm,
    JobsForm,
)


# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product'

# Jobs views
@login_required(login_url='login')
def create_jobs(request):
    forms = JobsForm()
    if request.method == 'POST':
        forms = JobsForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('jobs-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_jobs.html', context)


class JobsListView(ListView):
    model = Jobs
    template_name = 'store/jobs_list.html'
    context_object_name = 'jobs'


# Order views
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            product = forms.cleaned_data['product']
            company = forms.cleaned_data['company']
            customer = forms.cleaned_data['customer']
            phone = forms.cleaned_data['phone']
            email = forms.cleaned_data['email']
            size = forms.cleaned_data['size']
            papergramm = forms.cleaned_data['papergramm']
            price = forms.cleaned_data['price']
            count = forms.cleaned_data['count']
            jobs = forms.cleaned_data['jobs']
            Order.objects.create(
                company=company,
                customer=customer,
                phone=phone,
                email=email,
                product=product,
                size=size,
                papergramm=papergramm,
                price=price,
                jobs=jobs,
                count=count,
                status='pending'
            )
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_order.html', context)


class OrderListView(ListView):
    model = Order
    template_name = 'store/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all().order_by('-id')
        return context