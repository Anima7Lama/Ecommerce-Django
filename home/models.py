from django.db import models
STATUS = (('in', 'In Stock'),('out', 'Out Of Stock')) #create tuple inside tuple for choices

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True) #unique id 
    image = models.CharField(max_length=200, blank=True) #null

    def __str__(self):
        return self.name #show the category name instead of category id

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

class Item(models.Model):
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=200, unique=True) #unique id 
    price = models.IntegerField() 
    discounted_price = models.IntegerField(default=0) 
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    status = models.CharField(max_length=50, choices = STATUS)
    
    def __str__(self):
        return self.title

