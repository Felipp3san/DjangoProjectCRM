import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
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
            print(f"Password: {password}, User: {user}")
            return redirect('home')
    else:    
        user = request.user
        if user.is_authenticated:
            return redirect('tasks')
        else:
            return render(request, 'home.html', {})


@login_required
def logout_user(request):
    logout(request)
    messages.error(request, "You have been logged out...")
    return redirect('home')


@login_required
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


@staff_member_required
def users(request):
    if request.method == 'POST':
        pass
    else:
        users = User.objects.all()
        return render(request, 'users.html', {'users': users})
    

@staff_member_required
def add_user(request):
    if request.method == 'POST':
        form = forms.SignUpFormAdmin(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "New user added!")
            return redirect('users')
        else:
            messages.error(request, "An error has occurred when trying to add a new user.")
            print(form.errors) # for debugging
            return redirect('users')
    else:
        form = forms.SignUpFormAdmin()
        form.instance = False
        return render(request, 'add_edit_user.html', {'form': form})


@staff_member_required
def edit_user(request, user_id):

    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        form = forms.EditUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, "User data updated!")
            return redirect('users')
        else:
            messages.error(request, "An error has occurred when trying to update a user.")
            print(form.errors) # for debugging
            return redirect('users')
    else:
        form = forms.EditUserForm(instance=user)
        return render(request, 'add_edit_user.html', {'form': form})
    

@staff_member_required
def delete_user(request, user_id):

    user = User.objects.get(id=user_id)
    
    try:
        user.delete()
        messages.success(request, "User removed.")
    except:
        messages.success(request, "An error has occurred when trying to deleted an user.")
    return redirect('users')


@login_required
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
    

@staff_member_required
def tasks_admview(request, user_id):

    username = User.objects.get(pk=user_id)
    tasks = Task.objects.filter(user_id=user_id)

    if request.method == 'POST':
        content = request.POST['content']

        task = Task(content=content, user_id=user_id)
        task.save()

        return redirect('tasks_admview', user_id=user_id)
    else:
        return render(request, 'tasks_admview.html', {'tasks': tasks, 'username': username, 'user_id': user_id})
        

@login_required
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
    

@staff_member_required
def update_task_adminview(request, task_id, user_id):
    if request.method == 'POST':
        
        task = Task.objects.get(id=task_id)
        content = request.POST['content']
        task.content = content
    
        task.save()

        messages.success(request, "Task updated!")
        return redirect('tasks_admview', user_id=user_id)
    else:
        task = Task.objects.get(id=task_id)
        return render(request, 'update.html', {'task': task})


@login_required
def delete_task(request, task_id):
    task = Task.objects.filter(id=task_id)
    task.delete()
    messages.success(request, "Task deleted.")
    return redirect('tasks')


@staff_member_required
def delete_task_adminview(request, task_id, user_id):
    task = Task.objects.filter(id=task_id, user_id=user_id)
    task.delete()
    messages.success(request, "Task deleted.")
    return redirect('tasks_admview', user_id=user_id)


@login_required
def generate_task(request):
    url = 'https://www.boredapi.com/api/activity/'
    response = requests.get(url)

    data = response.json()
    user_id = request.user.id

    content = data["activity"]
    task = Task(content=content, user_id=user_id)
    task.save()

    return redirect('tasks')