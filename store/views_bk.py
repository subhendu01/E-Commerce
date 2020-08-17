from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models.product import Product
from .models.category import Category
from .models.cutomer import Customer
from django.views import View

# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()

    # print(request.GET)
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_product_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['category'] = categories

    return render(request,'index.html',{'products': data})

# # def validate_customer(customer):
# #     error_msg = None
# #     if not customer.first_name or len(customer.first_name) <= 4 or len(customer.first_name) >= 20:
# #         error_msg = 'First name required and must be 4-20 char'
# #
# #     elif not customer.last_name or len(customer.last_name) <= 1 or len(customer.last_name) >= 20:
# #         error_msg = 'Last name required and must be 1-20 char'
# #
# #     elif not customer.phone or len(customer.phone) < 10 or len(customer.phone) >= 20:
# #         error_msg = 'Phone number required and must be 10-20 digit'
# #
# #     elif not customer.email:
# #         error_msg = 'email required'
# #     elif customer.isExist():
# #         error_msg = "Email address already registered"
# #     elif not customer.password:
# #         error_msg = 'password required'
# #     return error_msg
#
# # def registerUser(request):
# #     try:
# #         postData = request.POST
# #         first_name = postData.get('firstname')
# #         last_name = postData.get('lastname')
# #         phone = postData.get('phone')
# #         email = postData.get('email')
# #         password = postData.get('password')
# #         # print(first_name, last_name, phone , email, password)
# #         error_msg = None
# #
# #         # customer details object
# #         customer = Customer(first_name=first_name,
# #                             last_name=last_name,
# #                             phone=phone,
# #                             email=email,
# #                             password=password)
# #
# #         # validation
# #         error_msg = validate_customer(customer)
# #         # save
# #         if not error_msg:
# #             # customer.save() // we can directly save the object by calling save() and we can do it by calling the register function
# #             customer.password = make_password(password)  # hashing password
# #             customer.register()
# #
# #             # return redirect('http://localhost:8000')
# #             return redirect('homepage')  # mapping the url
# #         else:
# #             data = {
# #                 'error': error_msg,
# #                 'values': {
# #                     "first_name": first_name,
# #                     "last_name": last_name,
# #                     "phone": phone,
# #                     "email": email
# #                 }
# #             }
# #             return render(request, 'signup.html', {'data': data})
# #     except Exception as e:
# #         print(str(e))
#
# # def signup(request):
# #     try:
# #         if request.method == 'GET':
# #             return render(request, 'signup.html')
# #         else:
# #             return registerUser(request)
# #     except Exception as e:
# #         print(str(e))
# # signup
# class signup(View):
#     def validate_customer(self,customer):
#         error_msg = None
#         if not customer.first_name or len(customer.first_name) <= 4 or len(customer.first_name) >= 20:
#             error_msg = 'First name required and must be 4-20 char'
#
#         elif not customer.last_name or len(customer.last_name) <= 1 or len(customer.last_name) >= 20:
#             error_msg = 'Last name required and must be 1-20 char'
#
#         elif not customer.phone or len(customer.phone) < 10 or len(customer.phone) >= 20:
#             error_msg = 'Phone number required and must be 10-20 digit'
#
#         elif not customer.email:
#             error_msg = 'email required'
#         elif customer.isExist():
#             error_msg = "Email address already registered"
#         elif not customer.password:
#             error_msg = 'password required'
#         return error_msg
#
#     def get(self,request):
#         try:
#             return render(request, 'signup.html')
#         except Exception as e:
#             print(str(e))
#
#     def post(self,request):
#         try:
#             postData = request.POST
#             first_name = postData.get('firstname')
#             last_name = postData.get('lastname')
#             phone = postData.get('phone')
#             email = postData.get('email')
#             password = postData.get('password')
#             # print(first_name, last_name, phone , email, password)
#
#             # customer details object
#             customer = Customer(first_name=first_name,
#                                 last_name=last_name,
#                                 phone=phone,
#                                 email=email,
#                                 password=password)
#             # validation
#             error_msg = self.validate_customer(customer)
#             # save
#             if not error_msg:
#                 # customer.save() // we can directly save the object by calling save() and we can do it by calling the register function
#                 customer.password = make_password(password)  # hashing password
#                 customer.register()
#
#                 # return redirect('http://localhost:8000')
#                 return redirect('homepage')  # mapping the url
#             else:
#                 data = {
#                     'error': error_msg,
#                     'values': {
#                         "first_name": first_name,
#                         "last_name": last_name,
#                         "phone": phone,
#                         "email": email
#                     }
#                 }
#                 return render(request, 'signup.html', {'data': data})
#         except Exception as e:
#             print(str(e))

# #login
# class login(View):
#     def get(self,request):
#         return render(request, 'login.html')
#     def post(self,request):
#         try:
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             customer = Customer.get_customer_by_email(email)
#             if customer:
#                 flag = check_password(password, customer.password)
#                 if flag:
#                     return redirect('homepage')
#                 else:
#                     error_msg = 'password  incorrect'
#                     return render(request, 'login.html', {'error': error_msg,'email': email})
#             else:
#                 error_msg = 'Email or password invalid'
#                 return render(request, 'login.html', {'error': error_msg})
#         except Exception as e:
#             print(str(e))
#             return render(request, 'login.html', {'error': str(e)})
# #login
# # def login(request):
# #     if request.method == 'GET':
# #         return render(request,'login.html')
# #     else:
# #         try:
# #             email = request.POST.get('email')
# #             password = request.POST.get('password')
# #             error_msg = None
# #             customer = Customer.get_customer_by_email(email)
# #             if customer:
# #                 print("111")
# #                 print(customer)
# #                 flag = check_password(password, customer.password)
# #                 print(flag)
# #                 if flag:
# #                     return redirect('homepage')
# #                 else:
# #                     error_msg = 'password  incorrect'
# #                     return render(request, 'login.html', {'error': error_msg})
# #             else:
# #                 error_msg = 'Email or password invalid'
# #                 return render(request,'login.html', {'error': error_msg})
# #         except Exception as e:
# #             print(str(e))
# #             return render(request, 'login.html', {'error': str(e)})

