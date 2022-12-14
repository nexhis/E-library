from django.db.models.signals import post_save 
from django.contrib.auth.models import User 
from django.dispatch import receiver 
from .models import Profile 

#to create a user profile for each user autmatically
@receiver(post_save, sender = User)
# checks if a user is created and then creates a profile to connect the two via the OneToOneField we just added.
def create_profile(sender, instance, created, **kwargs):   #function that runs everytime a user is created
    if created:     
        Profile.objects.create(user= instance)

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):  #save the profile everytime a user is saved
    instance.profile.save()
        



