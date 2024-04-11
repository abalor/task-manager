from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models
from django.urls import reverse

# def one_week_hence():
#     return timezone.now() + timezone.timedelta(days=7)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    reminder_time = models.IntegerField(default=1,null=False, blank=False)
    due_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created']
