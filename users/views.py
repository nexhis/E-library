from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm

#view function for register page 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  #save data in database
            username = form.cleaned_data.get('username')
            #create a one-time message once the user is registered 
            messages.success(request, f'Your account {username} has been created! You are now able to login') 
            return redirect('login')  #the user will be redirected to login page
    else:
        form = UserRegisterForm()
    return render(request, 'users/registerpage.html', {'form': form})

#decorator so the profile will be created only after the user is logged in
@login_required
#import the required forms and create instances of those forms depending on whether the request is get or post.
def profile(request):   
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})



