from django.urls import path,include
from .views import *
#from . import views
app_name = "home"

urlpatterns = [
    path('', HomeView.as_view(), name='home'), # HomeView = class name, .as_view() = indictaes a classview
    path('product-detail/<slug>', productDetailView.as_view(), name='product-detail'),
    # path('product-detail/<slug>/reviews', comment, name='reviews'),
    path('contact', contact, name='contact'),
    path('my-account', myAccount, name='myAccount'),
    path('product-list', ProductList.as_view(), name='productList'),

    path('search', searchView.as_view(), name = 'search'),
    path('category/<slug>', categoryView.as_view(), name = 'category'),
    #  path('brand/<name>', BrandView.as_view(), name = 'brand'),
    path('signup', register, name = 'signup'),
    path('signin', login, name = 'signin'),
    path('mycart', cartView.as_view(), name = 'mycart'),
    path('add-to-cart/<slug>', add_to_cart, name = 'add-to-cart'), #add to cart function
    path('delete-cart/<slug>', deleteCart, name = 'delete-cart'), #delete to cart function
    path('delete-single-cart/<slug>', remove_single_item_from_cart, name = 'delete-single-cart'), 
    path('checkout', checkoutView.as_view(), name = 'checkout'),
    path('payment', pay, name = 'payment'),
    # path('delete-single-cart/<slug>', deleteSingleCart, name = 'delete-single-cart'), #decrease quantity to cart function
    # path('cartsummary', cartSummaryView.as_view(), name = 'cartsummary'),
    # path('get-cart-total/', totalCart, name = 'total_cart'),
]