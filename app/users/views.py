from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})

def login(request):
    return render(request, 'users/login.html')
