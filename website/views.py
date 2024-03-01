import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from . import forms
from .models import Task, User

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('tasks')
        else:
            messages.error(request, "There was an error while trying to login. Please try again...")
            return redirect('home')
    else:    
        user = request.user
        if user.is_authenticated:
            return redirect('tasks')
        else:
            return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.error(request, "You have been logged out...")
    return redirect('home')


def account(request):
    return render(request, 'account.html', {})


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

            messages.success(request, "You have successfully registered! Welcome!")
            return redirect('tasks')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = forms.SignUpForm()
        return render(request, 'register.html', {'form': form})


def users(request):
    if request.method == 'POST':
        pass
    else:
        users = User.objects.all()
        return render(request, 'users.html', {'users': users})


def delete_user(request, user_id):
    pass


def edit_user(request, user_id):
    pass


def tasks(request):
    if request.method == 'POST':
        content = request.POST['content']
        user_id = request.user.id

        task = Task(content=content, user_id=user_id)
        task.save()

        return redirect('tasks')
    else:
        tasks = Task.objects.filter(user_id=request.user.id)
        return render(request, 'tasks.html', {'tasks': tasks})
    

def update_task(request, task_id):
    if request.method == 'POST':
        
        task = Task.objects.get(id=task_id)
        content = request.POST['content']
        task.content = content
    
        task.save()

        messages.success(request, "Your task was updated!")
        return redirect('tasks')
    else:
        task = Task.objects.get(id=task_id)
        return render(request, 'update.html', {'task': task})


def delete_task(request, task_id):
    task = Task.objects.filter(id=task_id)
    task.delete()
    return redirect('tasks')


def generate_task(request):
    url = 'https://www.boredapi.com/api/activity/'
    response = requests.get(url)

    data = response.json()
    user_id = request.user.id

    content = data["activity"]
    task = Task(content=content, user_id=user_id)
    task.save()

    return redirect('tasks')