from django.urls import path
from elibrary import views

urlpatterns = [
    path('', views.home, name='library-homepage'),
    path('about/', views.about, name='library-about'),
]