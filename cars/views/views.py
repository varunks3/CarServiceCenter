from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from ..models import *
from django.db.models import Sum
from django.urls import reverse
from django.views import  View



def home(request):
    return render(request,'index.html')

def aboutUs(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contact.html')

def services(request):
    services = Service.objects.all()
    return render(request,'services.html',{'services':services})


def add_to_cart(request, service_id):
    service = Service.objects.get(id=service_id)
    if not request.session.get('user'):
        return redirect('login')

    user_email = request.session.get('user')
    user = User.get_user_by_email(user_email)

    cart, created = Cart.objects.get_or_create(user=user, total_price=0)
    cart.services.add(service)
    cart.total_price += service.price
    cart.service_names = ", ".join([s.name for s in cart.services.all()])

    cart.save()


    return redirect('services')


def cart(request):
    cart_items = Cart.objects.all()
    total_price = cart_items.aggregate(total=Sum('total_price'))['total']
    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'cart.html', context)


def remove_item(request, item_id):
    cart_item = Cart.objects.get(id=item_id)
    cart_item.delete()
    return redirect(reverse('cart'))

def checkout(request):
    user_email = request.session.get('user')
    user = User.get_user_by_email(user_email)
    cart_items = Cart.objects.filter(user=user)

    order = Order.objects.create(total_price=0)

    for cart_item in cart_items:
        order.services.add(*cart_item.services.all())
        order.total_price += cart_item.total_price

    order.service_names = ", ".join([s.name for s in order.services.all()])
    order.save()

    cart_items.delete()

    return render(request, 'orders.html', {'order': order})

def orders_view(request):
    orders = Order.objects.all()
    service_names = [order.service_names for order in orders]
    return render(request, 'orders.html', {'service_names': service_names})


