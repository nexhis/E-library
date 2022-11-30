from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from users.models import Profile 
import datetime

#creating the book model for storing books in database
class Books(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    image = models.CharField(max_length=2083, blank=True, null=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title


    @staticmethod
    def get_books_by_id(ids):
        return Books.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_books():
        return Books.objects.all()



class Order(models.Model):
    product = models.ForeignKey(Books,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Profile,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
  
    def placeOrder(self):
        self.save()
  
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')