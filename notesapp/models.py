from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Note(models.Model):
    title = models.CharField(max_length = 50)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    allowed_users = models.CharField(max_length = 255)

    def __str__(self):
        return(f"{self.title}")
    
class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Note = models.ManyToManyField(Note)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MyUser.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.myuser.save()




    
# class NoteAccess(models.Model):
#     note = models.ManyToManyField(Note)
#     myusers = models.ManyToManyField(User)