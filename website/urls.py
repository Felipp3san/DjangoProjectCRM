from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('account/', views.account, name='account'),
    path('register/', views.register_user, name='register'),
    path('users/', views.users, name='users'),
    path('users/delete/<int:user_id>', views.delete_user, name='delete_user'),
    path('users/edit/<int:user_id>', views.edit_user, name='edit_user'),
    path('users/change_password/<int:user_id>', views.change_password, name='change_password'),
    path('users/add/', views.add_user, name='add_user'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:user_id>', views.tasks_admview, name='tasks_admview'),
    path('tasks/update/<int:task_id>', views.update_task, name='update_task'),
    path('tasks/update/<int:task_id>/<int:user_id>', views.update_task_adminview, name='update_task_adminview'),
    path('tasks/delete/<int:task_id>', views.delete_task, name='delete_task'),
    path('tasks/delete/<int:task_id>/<int:user_id>', views.delete_task_adminview, name='delete_task_adminview'),
    path('tasks/generate_tasks/', views.generate_task, name='generate_task'),   
]