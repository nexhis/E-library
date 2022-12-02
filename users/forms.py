from django import forms
from django.contrib.auth.models import User  #import User model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):  #create a new form that inherits from UserCreationForm
    email = forms.EmailField()  #adding the additional field "email"

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  #these are the fiels that will be shown in the form


# # interacts with the user model to let users update their username and email
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# #  interacts with the profile model to let users update their profile.
class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image', 'bio']  #the fields we want to work in 