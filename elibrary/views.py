from django.shortcuts import render
from .models import Books

# Create your views here.
books = [
    {
        'author': 'Aurelien Geron',
        'title': 'Hands-on machine learning with Scikit-Learn, Keras and Tensorflow',
        'category': 'Computer Science',
        'date_added': 'October 18, 2022'
    },
    {
        'author': 'Peter Norvig and Stuart J. Russell',
        'title': 'Artificial Intelligence - a modern approach',
        'category': 'Computer Science',
        'date_added': 'October 18, 2022'
    },
    {
        'author': 'Garry Kasparov',
        'title': 'Deep Thinking: Where Machine Intelligence Ends and Human Creativity Begins',
        'category': 'Computer Science',
        'date_added': 'October 17, 2022'
    }
]


def home(request):
    context = {
        'books': books
    }
    return render(request, 'elibrary/home.html', context)

def about(request):
    return render(request, 'elibrary/about.html')

def welcome(request):
    return render (request, 'elibrary/welcomepage.html')

