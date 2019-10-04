from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

from forum.models import Post

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            authenticate(username=form.cleaned_data['username'],
                         password=form.cleaned_data['password1'],
                        )
            auth_login(request, user)
            return redirect('forum-index')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})

def login(request):
    return render(request, 'users/login.html')

def profile(request, username=None):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile', username=request.user.username)

    else:
        context = {
            'posts': Post.objects.filter(author=User.objects.get(username=username))
        }

        if request.user.username == username:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

            context['u_form'] = u_form
            context['p_form'] = p_form
        
        if username is not None:
            user = User.objects.get(username=username)
            context['user'] = user

    return render(request, 'users/profile.html', context)
