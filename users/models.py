from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profilemodel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile')
    
    
    def __str__(self):
        return self.user.username
    