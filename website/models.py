from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    content = models.TextField(max_length=100)
    date_created = models.DateTimeField(default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)