from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('^post/$',views.post,name = 'post'),
    url('^messages/$',views.messages,name = 'messages'),
    url('^update/profile/$',views.update_profile,name = 'about'),
    url('^send/$',views.send_message,name = 'about'),
    url('^help/$',views.help,name = 'help'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 