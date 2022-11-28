from django.shortcuts import render
from .models import Books
# Create your views here.


def home(request):
    
    return render(request, 'elibrary/home.html')

def about(request):
    
    return render(request, 'elibrary/about.html')

def welcome(request):
    books = Books.objects.all() 
    return render (request, 'elibrary/welcome.html', {'books': books})
