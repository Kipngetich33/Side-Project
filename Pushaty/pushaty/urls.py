from django.conf.urls import url
from . import views
from django.conf import settings


urlpatterns=[
    url('^$',views.home,name = 'Home'),
    url('^post/$',views.post,name = 'Post'),
    url('^messages/$',views.messages,name = 'Messages'),
]