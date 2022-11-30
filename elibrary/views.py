from django.shortcuts import render
from .models import Books
from django.views import  View
# Create your views here.


def home(request):
    
    return render(request, 'elibrary/home.html')

def about(request):
    
    return render(request, 'elibrary/about.html')

def welcome(request):
    books = Books.objects.all() 
    return render (request, 'elibrary/welcome.html', {'books': books})

def cart(request):
    
    return render(request, 'elibrary/cart.html')