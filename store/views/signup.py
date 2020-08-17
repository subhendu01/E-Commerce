from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.cutomer import Customer
from django.views import View

# def validate_customer(customer):
#     error_msg = None
#     if not customer.first_name or len(customer.first_name) <= 4 or len(customer.first_name) >= 20:
#         error_msg = 'First name required and must be 4-20 char'
#
#     elif not customer.last_name or len(customer.last_name) <= 1 or len(customer.last_name) >= 20:
#         error_msg = 'Last name required and must be 1-20 char'
#
#     elif not customer.phone or len(customer.phone) < 10 or len(customer.phone) >= 20:
#         error_msg = 'Phone number required and must be 10-20 digit'
#
#     elif not customer.email:
#         error_msg = 'email required'
#     elif customer.isExist():
#         error_msg = "Email address already registered"
#     elif not customer.password:
#         error_msg = 'password required'
#     return error_msg

# def registerUser(request):
#     try:
#         postData = request.POST
#         first_name = postData.get('firstname')
#         last_name = postData.get('lastname')
#         phone = postData.get('phone')
#         email = postData.get('email')
#         password = postData.get('password')
#         # print(first_name, last_name, phone , email, password)
#         error_msg = None
#
#         # customer details object
#         customer = Customer(first_name=first_name,
#                             last_name=last_name,
#                             phone=phone,
#                             email=email,
#                             password=password)
#
#         # validation
#         error_msg = validate_customer(customer)
#         # save
#         if not error_msg:
#             # customer.save() // we can directly save the object by calling save() and we can do it by calling the register function
#             customer.password = make_password(password)  # hashing password
#             customer.register()
#
#             # return redirect('http://localhost:8000')
#             return redirect('homepage')  # mapping the url
#         else:
#             data = {
#                 'error': error_msg,
#                 'values': {
#                     "first_name": first_name,
#                     "last_name": last_name,
#                     "phone": phone,
#                     "email": email
#                 }
#             }
#             return render(request, 'signup.html', {'data': data})
#     except Exception as e:
#         print(str(e))

# def signup(request):
#     try:
#         if request.method == 'GET':
#             return render(request, 'signup.html')
#         else:
#             return registerUser(request)
#     except Exception as e:
#         print(str(e))
# signup
class signup(View):
    def validate_customer(self,customer):
        error_msg = None
        if not customer.first_name or len(customer.first_name) <= 4 or len(customer.first_name) >= 20:
            error_msg = 'First name required and must be 4-20 char'

        elif not customer.last_name or len(customer.last_name) <= 1 or len(customer.last_name) >= 20:
            error_msg = 'Last name required and must be 1-20 char'

        elif not customer.phone or len(customer.phone) < 10 or len(customer.phone) >= 20:
            error_msg = 'Phone number required and must be 10-20 digit'

        elif not customer.email:
            error_msg = 'email required'
        elif customer.isExist():
            error_msg = "Email address already registered"
        elif not customer.password:
            error_msg = 'password required'
        return error_msg

    def get(self,request):
        try:
            return render(request, 'signup.html')
        except Exception as e:
            print(str(e))

    def post(self,request):
        try:
            postData = request.POST
            first_name = postData.get('firstname')
            last_name = postData.get('lastname')
            phone = postData.get('phone')
            email = postData.get('email')
            password = postData.get('password')
            # print(first_name, last_name, phone , email, password)

            # customer details object
            customer = Customer(first_name=first_name,
                                last_name=last_name,
                                phone=phone,
                                email=email,
                                password=password)
            # validation
            error_msg = self.validate_customer(customer)
            # save
            if not error_msg:
                # customer.save() // we can directly save the object by calling save() and we can do it by calling the register function
                customer.password = make_password(password)  # hashing password
                customer.register()

                # return redirect('http://localhost:8000')
                return redirect('homepage')  # mapping the url
            else:
                data = {
                    'error': error_msg,
                    'values': {
                        "first_name": first_name,
                        "last_name": last_name,
                        "phone": phone,
                        "email": email
                    }
                }
                return render(request, 'signup.html', {'data': data})
        except Exception as e:
            print(str(e))