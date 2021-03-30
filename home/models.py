from django.db import models
STATUS = (('in', 'In Stock'),('out', 'Out Of Stock')) #create tuple inside tuple for choices
LABEL = (('new', 'New Product'),('hot', 'Hot Product'),('sales', 'Product in sale'))

from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True) #unique id 
    image = models.ImageField(upload_to = 'media') 

    def __str__(self):
        return self.name #show the category name instead of category id
    
    def get_category_url(self):
        return reverse("home:category", kwargs={'slug':self.slug})

class Slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'media') 
    description = models.TextField()
    url = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=300)
    rank = models.IntegerField(unique=True) 
    image = models.ImageField(upload_to = 'media') 
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# class Brand(models.Model):
#     name = models.CharField(max_length=300)
#     rank = models.IntegerField(unique=True) 
#     image = models.ImageField(upload_to = 'media') 

#     def __str__(self):
#         return self.name
    
#     def get_brand_url(self):
#         return reverse("home:brand", kwargs={'name':self.name})

class Item(models.Model):
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=200, unique=True) #unique id 
    item_code = models.CharField(max_length=100, blank=True) 
    price = models.FloatField() 
    discounted_price = models.FloatField(default=0) 
    description = RichTextField(blank=True, null=True)
    # description = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    # brand = models.ForeignKey(Brand, on_delete = models.CASCADE, blank=True)
    status = models.CharField(max_length=50, choices = STATUS)
    label = models.CharField(max_length=50, choices = LABEL, default='new')
    image = models.ImageField(upload_to = 'media') 

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("home:product-detail", kwargs={'slug':self.slug}) #if you want to pass ceratin dictionary to another page
    
    def get_cart_url(self):
        return reverse("home:add-to-cart", kwargs={'slug':self.slug}) # slug value is in item, so the function is made in item model.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=300, null=True)
    email = models.EmailField(max_length=300, null=True)

    def __str__(self):
        return self.name 

class OrderItem(models.Model):
    slug = models.CharField(max_length=200, null=True)
    user = models.CharField(max_length=200, blank=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True) 
    # order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True) 
    quantity = models.IntegerField(default=1)
    total = models.IntegerField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # items = models.ManyToManyField(OrderedItem)
    # item = models.ForeignKey(Item, on_delete = models.CASCADE)
    # slug = models.CharField(max_length=200)
    # quantity = models.IntegerField(default=1)
    # user = models.CharField(max_length=200)
    # date = models.DateTimeField(auto_now=True)
    # total = models.IntegerField(null=True)

    def __str__(self):
        return self.item.title

    def delete_cart_url(self):
        return reverse("home:delete-cart", kwargs={'slug':self.slug})
    
    def delete_single_cart_url(self):
        return reverse("home:delete-single-cart", kwargs={'slug':self.slug})

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField(auto_now_add=True) #we can change the value whenever the order is set to complete
    ordered = models.BooleanField(default=False) 
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.customer.username
    
    @property
    def get_cart_total(self):
        total = 0
        for order_item in self.items.all():
            total = sum(order_item.total)
        
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True) 
    # order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True) 
    address = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=300, null=True)
    state = models.CharField(max_length=300, null=True)
    zipcode = models.CharField(max_length=300, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.address
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
