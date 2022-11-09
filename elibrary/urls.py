from django.urls import path
from elibrary import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='library-homepage'),
=======
    path('', views.welcome, name='library'),
    path('home/', views.home, name='library-homepage'),
>>>>>>> WIN-26-Custom_user_profile
    path('about/', views.about, name='library-about'),
]