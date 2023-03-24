from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
User: name, first_name, last_name, password
Account: avatar
OneToOne
"""
class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='account')
    avatar=models.ImageField(upload_to='avatars/')
    
    """account.user"""
    
    def __str__(self):
        return self.user.username
    
