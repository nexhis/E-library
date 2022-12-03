from django.contrib import admin
from mysite.books.models import Student, bookborrowed, Book

class DisplayAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

admin.site.register(student)
admin.site.register(bookborrowed, duedate)
admin.site.register(Book)