from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    created = models.DateField(auto_now_add = True,null = True)
    user = models.ForeignKey(User,null = True)
    message = models.CharField(max_length = 200,null = True)

    def __unicode__(self):
        return self.message
