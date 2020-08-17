from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.cutomer import Customer
from django.views import View

#login
class Login(View):
    return_url = None
    def get(self,request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
    def post(self,request):
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            customer = Customer.get_customer_by_email(email)
            if customer:
                flag = check_password(password, customer.password)
                if flag:
                    request.session['customer'] = customer.id

                    # forwarding to the same page where it showing login page
                    if Login.return_url:
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        Login.return_url = None
                        return redirect('homepage')
                else:
                    error_msg = 'password  incorrect'
                    return render(request, 'login.html', {'error': error_msg,'email': email})
            else:
                error_msg = 'Email or password invalid'
                return render(request, 'login.html', {'error': error_msg})
        except Exception as e:
            print(str(e))
            return render(request, 'login.html')
#login
# def login(request):
#     if request.method == 'GET':
#         return render(request,'login.html')
#     else:
#         try:
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             error_msg = None
#             customer = Customer.get_customer_by_email(email)
#             if customer:
#                 print("111")
#                 print(customer)
#                 flag = check_password(password, customer.password)
#                 print(flag)
#                 if flag:
#                     return redirect('homepage')
#                 else:
#                     error_msg = 'password  incorrect'
#                     return render(request, 'login.html', {'error': error_msg})
#             else:
#                 error_msg = 'Email or password invalid'
#                 return render(request,'login.html', {'error': error_msg})
#         except Exception as e:
#             print(str(e))
#             return render(request, 'login.html', {'error': str(e)})

#logout
def logout(request):
    request.session.clear()
    return redirect('login')
