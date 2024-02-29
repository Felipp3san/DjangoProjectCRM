from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import forms
from .models import Task, User

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
            return redirect('tasks')
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