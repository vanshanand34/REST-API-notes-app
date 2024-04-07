from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length = 50)
    creater = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    allowed_users = models.CharField(max_length = 255)

    def __str__(self):
        return(f"{self.title}")