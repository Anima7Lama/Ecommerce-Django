from django.urls import path,include
from .views import *
#from . import views
app_name = "home"

urlpatterns = [
    path('', HomeView.as_view(), name='home'), # HomeView = class name, .as_view() = indictaes a classview
    path('product-detail/<slug>', productDetailView.as_view(), name='product-detail'),
    path('contact', contact, name='contact'),
    path('checkout', checkout, name='checkout'),
    path('cart', cart, name='cart'),
    path('login', login, name='login'),
    path('my-account', myAccount, name='myAccount'),
    path('product-list', ProductList.as_view(), name='productList'),

    path('search', searchView.as_view(), name = 'search'),
    path('category/<slug>', categoryView.as_view(), name = 'category'),
]