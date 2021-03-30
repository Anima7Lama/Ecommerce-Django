from django.contrib import admin
from .models import *
from csvexport.actions import csvexport

#customizing admin panel
class item(admin.ModelAdmin):
    list_display = ("title","item_code","price","discounted_price","category","label","image")
    search_fields = ["title","description"]
    list_filter = ("category","label","price")
    list_per_page = 6
    actions = [csvexport]

class category(admin.ModelAdmin):
    list_display = ("name","slug","image")
    search_fields = ["name"]
    list_per_page = 5

# Register your models here.
admin.site.register(Item, item)
admin.site.register(Category, category)
admin.site.register(Ad)
# admin.site.register(Brand)
admin.site.register(Slider)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Contact)
