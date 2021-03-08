from django.db import models
STATUS = (('in', 'In Stock'),('out', 'Out Of Stock')) #create tuple inside tuple for choices
LABEL = (('new', 'New Product'),('hot', 'Hot Product'),('sales', 'Product in sale'))

from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True) #unique id 
    image = models.CharField(max_length=200, blank=True) #null

    def __str__(self):
        return self.name #show the category name instead of category id
    
    def get_category_url(self):
        return reverse("home:category", kwargs={'slug':self.slug})

class Slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.TextField()
    description = models.TextField()
    url = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=300)
    rank = models.IntegerField(unique=True) 
    image = models.TextField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=300)
    rank = models.IntegerField(unique=True) 
    image = models.TextField()

    def __str__(self):
        return self.name
    
    def get_brand_url(self):
        return reverse("home:brand", kwargs={'name':self.name})

class Item(models.Model):
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=200, unique=True) #unique id 
    item_code = models.CharField(max_length=100, blank=True) 
    price = models.IntegerField() 
    discounted_price = models.IntegerField(default=0) 
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    status = models.CharField(max_length=50, choices = STATUS)
    label = models.CharField(max_length=50, choices = LABEL, default='new')
    image = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("home:product-detail", kwargs={'slug':self.slug}) #if you want to pass ceratin dictionary to another page
    
    def get_cart_url(self):
        return reverse("home:add-to-cart", kwargs={'slug':self.slug}) # slug value is in item, so the function is made in item model.
    
class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    slug = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    user = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    total = models.IntegerField(null=True)

    def __str__(self):
        return self.title

    def delete_cart_url(self):
        return reverse("home:delete-cart", kwargs={'slug':self.slug})
    
    def delete_single_cart_url(self):
        return reverse("home:delete-single-cart", kwargs={'slug':self.slug})

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
