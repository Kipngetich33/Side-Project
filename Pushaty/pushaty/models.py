from django.db import models

# Create your models here.

class Chat(models.Model):
    created = models.DateField(auto_now_add = True)
    user = models.ForeignKey(User)
    message = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.message
