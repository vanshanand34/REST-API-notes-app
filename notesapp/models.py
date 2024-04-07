from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Note(models.Model):
    title = models.CharField(max_length = 50)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    allowed_users = models.CharField(max_length = 255)

    def __str__(self):
        return(f"{self.title}")
