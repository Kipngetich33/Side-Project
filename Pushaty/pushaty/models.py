from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    '''
    Class profile that creates the profile objects
    '''
    created = models.DateField(auto_now_add = True,null = True)
    user = models.ForeignKey(User,null = True)
    username = models.CharField(max_length = 50,null = True)
    email = models.EmailField(null = True)
    
    def __unicode__(self):
        return self.username

class Chat(models.Model):
    '''
    Class model that creates the Chat objects
    '''
    created = models.DateField(auto_now_add = True,null = True)
    user = models.ForeignKey(User,null = True)
    recipient = models.ForeignKey(Profile,null = True)
    message = models.CharField(max_length = 200,null = True)

    def __unicode__(self):
        return self.message
