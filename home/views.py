from django.shortcuts import render, redirect
from .models import Category, Slider, Ad, Item, Customer, OrderItem, Order, ShippingAddress, Contact

# Create your views here.
from django.views.generic.base import View

from django.contrib.auth.models import User
from django.contrib import messages,auth

from django.core.mail import EmailMultiAlternatives #for email

#Class based view
class BaseView(View):   #BaseView(View) = classname(View class inherited form django)
    views = {}

class HomeView(BaseView):
    def get(self,request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['ads1'] = Ad.objects.filter(rank = 1)
        self.views['ads2'] = Ad.objects.filter(rank = 2)
        self.views['ads3'] = Ad.objects.filter(rank = 3)
        self.views['ads4'] = Ad.objects.filter(rank = 4)
        self.views['ads5'] = Ad.objects.filter(rank = 5)
        self.views['ads6'] = Ad.objects.filter(rank = 6)
        self.views['items'] = Item.objects.all()
        self.views['new_items'] = Item.objects.filter(label='new')
        self.views['hot_items'] = Item.objects.filter(label='hot')
        self.views['sale_items'] = Item.objects.filter(label='sales')
        return render(request, 'index.html', self.views)

class ProductList(BaseView):
    def get(self,request):
        self.views['productLists'] = Item.objects.all()
        self.views['categories'] = Category.objects.all()
        return render(request, 'product-list.html',self.views)

class productDetailView(BaseView):
    def get(self,request,slug): #slug will be passed as id as slug is unique value
        category = Item.objects.get(slug=slug).category
        self.views['related_items'] = Item.objects.filter(category=category)
        self.views['item_detail'] = Item.objects.filter(slug = slug)
        self.views['categories'] = Category.objects.all()
        # self.views['brands'] = Brand.objects.all()
        return render(request, 'product-detail.html',self.views)

class searchView(BaseView):
    def get(self,request):
        query = request.GET.get('query',None) #get function takes the query value from the form
        if not query:
            return redirect('/')
        self.views['search_query'] = Item.objects.filter(
            description__icontains = query
        )
        self.views['searched_for'] = query
        return render(request, 'search.html',self.views)

class categoryView(BaseView):
    def get(self,request,slug):
        cat = Category.objects.get(slug = slug).id
        self.views['category_items'] = Item.objects.filter(category = cat)
        return render(request, 'category.html', self.views)

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'The username is already used.')
                return redirect('home:signup')
            
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'The email is already used.')
                return redirect('home:signup')
            
            else:
                data = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                    email = email,
                    password = password,
                )
                data.save()
                messages.error(request, 'You have successfully signed up.')
                return redirect('home:signup')
        else:
            messages.error(request, 'The password did not match.')
            return redirect('home:signup')
        
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        
        if user is None:
            messages.error(request, 'Username and password didnot match')
            return redirect('home:signin')
        else:
            auth.login(request,user)
            if user.is_superuser:
                return redirect('/admin')  
            else:
                return redirect('/')
        
    return render(request, 'signin.html')

class cartView(BaseView):
    def get(self, request):
        self.views['carts'] = OrderItem.objects.filter(user = request.user.username)
        
        return render(request, 'cart.html', self.views)

# def cart(requset):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=false)
#         items = order.orderitem_set.all() #Returns all OrderItem objects related to Order.
#     else:
#         items = []
    
#     context = {'carts':cart}
#     return render(request, 'cart.html', context)

# increase the quantity and update the total | fillup the cart infos
def cart(request,slug):
    if OrderItem.objects.filter(slug=slug, user= request.user.username).exists():
        quantity = OrderItem.objects.get(slug=slug, user= request.user.username).quantity
        quantity = quantity +1
        price = Item.objects.get(slug=slug).price
        discounted_price = Item.objects.get(slug=slug).discounted_price
        if discounted_price > 0:
            total = quantity*discounted_price
            OrderItem.objects.filter(slug=slug, user= request.user.username).update(quantity = quantity)
        else:
            total = quantity*price
        OrderItem.objects.filter(slug=slug, user= request.user.username).update(quantity = quantity, total = total)
    
    else:
        price = Item.objects.get(slug=slug).price
        discounted_price = Item.objects.get(slug=slug).discounted_price
        if discounted_price > 0:
            total = discounted_price
        else:
            total = price
        data = OrderItem.objects.create(
            user = request.user.username,
            slug = slug,
            item = Item.objects.filter(slug=slug)[0], # [0] = the first element inside the list
            total = total
        )
        data.save()
    return redirect('home:mycart')

def get_total_cart(request):
    if OrderItem.objects.filter(user= request.user.username).exists():
        total = OrderItem.objects.get(user= request.user.username).total
        subtotal = sum([Cart.total for cart in Cart])

#reduce quantity and update the total
def deleteSingleCart(request,slug):
    if OrderItem.objects.filter(slug=slug, user= request.user.username).exists():
        quantity = OrderItem.objects.get(slug=slug, user= request.user.username).quantity
        quantity = quantity -1
        price = Item.objects.get(slug=slug).price
        discounted_price = Item.objects.get(slug=slug).discounted_price
        if discounted_price > 0:
            total = quantity*discounted_price
            OrderItem.objects.filter(slug=slug, user= request.user.username).update(quantity = quantity)
        else:
            total = quantity*price
        OrderItem.objects.filter(slug=slug, user= request.user.username).update(quantity = quantity, total = total)

        return redirect('home:mycart')

def deleteCart(request,slug):
    if OrderItem.objects.filter(slug=slug, user= request.user.username).exists():
        OrderItem.objects.filter(slug=slug, user= request.user.username).delete()
        messages.success(request, 'The item is deleted')
    return redirect('home:mycart')

class cartSummaryView(BaseView):
    def get(self, request):
        self.views['Total'] = Order.objects.filter(user = request.user.username)
        
        return render(request, 'cart.html', self.views)
# class BrandView(BaseView):
#     def get(self,request,name):
#         cat = Brand.objects.get(name = name).id
#         self.views['brand_items'] = Item.objects.filter(brand = cat)
#         return render(request, 'brand.html', self.views)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        messages.success(request, 'Your message is sent.')
        text_content = 'This is an important message.'
        html_content = f"<p> The customer having name {name} , email address {email} of subject {subject} has a message {message}.</p>"
                                                               #from (smpt server email)  #to
        message = EmailMultiAlternatives(subject, text_content, 'taeanee101@gmail.com', ['taeanee101@gmail.com']) 
        message.attach_alternative(html_content, "text/html")
        message.send()
    return render(request, 'contact.html')

def checkout(request):
    return render(request, 'checkout.html')

def myAccount(request):
    return render(request, 'my-account.html')

def wishlist(request):
    return render(request, 'wishlist.html')

#-------------------------------------------------API---------------------------------------------------
from rest_framework import viewsets
from . serializers import *
# ViewSets define the view behavior.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = CartSerializer

from django.views.generic import View, DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter, SearchFilter
class ItemFilterListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ['id','title','price','label','category']
    ordering_fields = ['price','title','id']
    search_fields = ['title','description']
