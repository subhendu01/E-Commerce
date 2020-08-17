from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product

class Cart(View):
    def get(self,request):
        try:
            print('id', request.session.get('cart').keys())
            ids  = list(request.session.get('cart').keys())
            products = Product.get_products_by_id(ids)
            return render(request, 'cart.html',{'products': products})
        except Exception as e:
            print('2222')
            print(str(e))
            # return render(request, 'cart.html')