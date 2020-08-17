from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.orders import Orders
from store.models.cutomer import Customer
from django.views import View
from store.middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator


class OrdersView(View):

    # @method_decorator(auth_middleware)
    def get(self,request):
        customer = request.session.get('customer')
        orders = Orders.get_orders_by_customer(customer)
        print(orders)
        orders = orders.reverse()
        return render(request, 'orders.html',{'orders':orders})
