from django.contrib import admin
from django.urls import path
from . import views
# from .views.home import store
# from .views.signup import Signup
# from .views.login import Login , logout
# from .views.cart import Cart
# from .views.checkout import CheckOut
# from .views.orders import OrderView
# from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', views.index, name='index'),
    # path('store', store , name='store'),

    path('signup/', views.signup, name='signup'),
    path('login/',views.login,name='login')
    # path('logout', logout , name='logout'),
    # path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    # path('check-out', CheckOut.as_view() , name='checkout'),
    # path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
