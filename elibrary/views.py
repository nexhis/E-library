from django.shortcuts import render
from .models import *
from django.views import  View
# Create your views here.


def home(request):
    books = Books.objects.all()
    
    return render(request, 'elibrary/home.html', {'books': books})

def about(request):
    
    return render(request, 'elibrary/about.html')

def welcome(request):
    return render (request, 'elibrary/welcome.html')

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
    else:
        items = []

    context = {'items': items, 'order':order}
    
    return render(request, 'elibrary/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
    else:
        items = []

    context = {'items': items, 'order':order}
    
    return render(request, 'elibrary/checkout.html',context)
