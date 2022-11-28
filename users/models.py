from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    major = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    # city = models.CharField(max_length=50)


    def __str__(self):
        return f' {self.user.username} Profile'




