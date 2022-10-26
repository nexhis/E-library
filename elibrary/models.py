from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Books(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

    class BookInstance(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="Book unique id across the Library")
    book=models.ForeignKey('Book', on_delete=models.CASCADE,null=True)
    book_number=models.PositiveIntegerField(null=True,help_text="Book number for books of the save kind")
    Is_borrowed = models.BooleanField(default=False)
        def __str__(self):
        return f"{self.id} {self.book}"
    
    def get_returndate():
    return datetime.today() + timedelta(days=15)
    
