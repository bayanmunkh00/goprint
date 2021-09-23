from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Product, Order, Jobs


@login_required(login_url='login')
def dashboard(request):
    total_product = Product.objects.count()
    total_oder = Order.objects.count()
    total_jobs = Jobs.objects.count()
    orders = Order.objects.all().order_by('-id')
    context = {
        'product': total_product,
        'order': total_oder,
        'orders': orders,
        'jobs': total_jobs
    }
    return render(request, 'dashboard.html', context)
