from django.db import models
from django.db.models.deletion import CASCADE, PROTECT

class Customer(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    password = models.CharField(max_length=15, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    CATEGORIES = (
        ('Food', 'Food'),
        ('Electronics', 'Electronics'),
        ('Sports', 'Sports'),
        ('Health & Beauty', 'Health & Beauty'),
        ('Household', 'Household'),
        ('Appliances', 'Appliances'),
        ('Furniture', 'Furniture'),
        ('Outdoors', 'Outdoors'),
        ('Clothing', 'Clothing'),
        ('Misc.', 'Misc.')
    )
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORIES)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    img_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, on_delete=PROTECT, null=True)
    item = models.ForeignKey(Item, on_delete=CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)