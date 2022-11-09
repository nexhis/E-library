from django.db import models
<<<<<<< HEAD

# Create your models here.

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

=======
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    major = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)

    def __str__(self):
        return f' {self.user.username} Profile'


>>>>>>> WIN-26-Custom_user_profile

