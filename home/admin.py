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

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer',
                    'ordered',
                    'shipping_address',
                    'billing_address',
                    ]
    list_display_links = [
        'customer',
        'shipping_address',
        'billing_address',
    ]
    list_filter = ['ordered']
    search_fields = [
        'customer__username']

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'customer',
        'street_address',
        'apartment_address',
        'city',
        'country',
        'zipcode',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['customer', 'street_address', 'apartment_address', 'zipcode']

# Register your models here.
admin.site.register(Item, item)
admin.site.register(Category, category)
admin.site.register(Ad)
# admin.site.register(Brand)
admin.site.register(Slider)
# admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Address, AddressAdmin)
admin.site.register(Contact)
