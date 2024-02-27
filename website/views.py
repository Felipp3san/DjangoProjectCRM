from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import forms

def home(request):
    #Logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.error(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:    
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.error(request, "You Have Been Logged Out...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            #Authenticate
            user = authenticate(request, username=username, password=password)
            login(request, user)

            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = forms.SignUpForm()
        return render(request, 'register.html', {'form': form})
