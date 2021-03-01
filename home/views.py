from django.shortcuts import render, redirect
from .models import Category, Slider, Ad, Brand, Item

# Create your views here.
from django.views.generic.base import View

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
        self.views['brands'] = Brand.objects.all()
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

def contact(request):
    return render(request, 'contact.html')

def checkout(request):
    return render(request, 'checkout.html')

def cart(request):
    return render(request, 'cart.html')

def login(request):
    return render(request, 'login.html')

def myAccount(request):
    return render(request, 'my-account.html')

def wishlist(request):
    return render(request, 'wishlist.html')
