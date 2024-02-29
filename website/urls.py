from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('users/', views.users, name='users'),
    path('users/delete/<int:user_id>', views.delete_user, name='delete_user'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/update/<int:task_id>', views.update_task, name='update_task'),
    path('tasks/delete/<int:task_id>', views.delete_task, name='delete_task'),

]