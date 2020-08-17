from django.contrib import admin
from django.urls import path
from .views.login import Login,logout
from .views.signup import signup
from .views.home import Index
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.ordersview import OrdersView
from store.middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name = 'homepage'),
    # path('signup', signup), #when calling as defination
    path('signup', signup.as_view(), name = 'signup'), # when calling as class
    path('login', Login.as_view(), name ='login'),
    path('logout',logout),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrdersView.as_view()), name='orders')
]
