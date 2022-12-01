from django.contrib import admin
from .models import Profile
from elibrary.models import Books, Order, Customer,OrderItem,ShippingAddress

#register our models so the admin can see them in his admin page
admin.site.register(Profile)

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock')  #these are the fields of the books we want to show to the admin page

admin.site.register(Books, BooksAdmin)

admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


