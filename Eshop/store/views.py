from django.shortcuts import render,redirect
from .models import Product
from .models import Category
from.models import Customer
from django.contrib.auth.hashers import make_password  ##PASSWORD HASHING
from django.contrib.auth.hashers import check_password


def index(request):
    products=None
    categories=Category.get_all_categories()
    categoryID=request.GET.get('category')
    if categoryID:
        products=Product.get_all_products_by_categoryid(categoryID)
    else:
        products=Product.get_all_products()
    data={}
    data['products']=products
    data['categories']=categories

    return render(request,'index.html',data)

#SIGN UP PAGE:
# views.py


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        # Check if a customer with the provided email already exists
        existing_customer = Customer.objects.filter(email=email).first()

        if existing_customer:
            # If the email already exists, show an error message
            error_message = 'Email Address Already Registered.'
            return render(request, 'signup.html', {'error': error_message})

        # If the email does not exist, create a new Customer instance
        user = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        user.password = make_password(password)  # Fix: use `password` instead of `customer.password####Password Hashing`
        user.save()

        return render(request, 'signup.html')

    return render(request, 'signup.html')



###LOGIN PAGE###
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                return redirect('index')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        return render(request, 'login.html', {'error': error_message})

    return render(request, 'login.html')

# Create your views here.
