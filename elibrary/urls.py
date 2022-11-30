from django.urls import path
from elibrary import views
from django.urls import path
from elibrary import views  #importing the views methods for the welcome, home and about page

#defining the path for the website main buttons

urlpatterns = [
    path('', views.welcome, name='library'),
    path('home/', views.home, name='library-homepage'),
    path('about/', views.about, name='library-about'),
    path('cart/', views.cart, name='cart'),
]