from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here which will create out tables in the database

#Database model for users'profile in the system 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #onetoone relationship, means that one user can have one profile and vice versa
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    major = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)


    def __str__(self):
        return f' {self.user.username} Profile'

#resize the large uploaded images
    def save(self):
        super().save()  #the method runs of the parent class

        img = Image.open(self.image.path) #it will open the image of the current instance

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)  #will save in the same path and override the large image

