from django import forms
from . models import Chat, Profile
from django.contrib.auth.forms import AuthenticationForm


class ProfileUpdateForm(forms.Form):
    '''
    classs that creates profile update form
    ''' 
    username = forms.CharField(label='Username',max_length = 30)
    email = forms.EmailField(null=True)
    bio = forms.CharField(label='Bio',max_length=500)

    # the line is line below is currently commented out because the image setting dependencies do not exist yet
    # profile_photo = forms.ImageField(label = 'Image Field') 
    