from django.contrib import admin
from django.urls import path
from .views.signup import *
from .views.login import *
from .views.views import *


urlpatterns = [
    path('',home),
    path('aboutUs',aboutUs),
    path('contact',contact),
    path('services',services, name='services'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('add_to_cart/<int:service_id>', add_to_cart, name='add_to_cart'),
    path('cart', cart, name='cart'),
    path('remove-item/<int:item_id>/', remove_item, name='remove_item'),
    path('checkout', checkout, name='checkout'),
    path('orders/', orders_view, name='orders'),

    # path('order/', orders, name='order'),
    # path('orders/', orders, name='orders'),
]
