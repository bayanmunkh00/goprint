from django.db import models

from users.models import User
class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    sortno = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Jobs(models.Model):
    name = models.CharField(max_length=120, unique=True)
    sortno = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    company = models.CharField(max_length=60)
    customer = models.CharField(max_length=60)
    phone = models.IntegerField()
    email = models.CharField(max_length=40)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.IntegerField()
    papergramm = models.IntegerField()
    price = models.IntegerField()
    count = models.IntegerField()
    jobs = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name
