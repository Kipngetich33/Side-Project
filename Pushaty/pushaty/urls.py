from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('^post/$',views.post,name = 'post'),
    url('^messages/$',views.messages,name = 'messages'),
    url('^about/$',views.about,name = 'about'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 