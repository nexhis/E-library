from django.db.models.signals import post_save 
from django.contrib.auth.models import User 
from django.dispatch import receiver 
from .models import Profile 

#to create a user profile for each user autmatically
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):   #function that runs everytime a user is created
    if created:     
        Profile.objects.create(user= instance)

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
        



