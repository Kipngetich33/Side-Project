from django import forms
from . models import Chat, Profile
from django.contrib.auth.forms import AuthenticationForm


class ProfileUpdateForm(forms.Form):
    '''
    classs that creates profile update form
    ''' 
    username = forms.CharField(label='Username',max_length = 30)
    email = forms.EmailField()
    bio = forms.CharField(label='Bio',max_length=500)

    # the line is line below is currently commented out because the image setting dependencies do not exist yet
    # profile_photo = forms.ImageField(label = 'Image Field') 

class HelpForm(forms.Form):
    '''
    classs that creates the form that allows the user to send a proposal for help from pushaty
    ''' 
    name = forms.CharField(label='First Name',max_length = 30)
    email = forms.EmailField()
    desciption = forms.CharField(label='Bio',max_length=500)
    extra_information = forms.CharField(label='More Information',max_length=500)
    # there should be fields for files and links here they will be added later