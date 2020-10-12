from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url(r'^image',views.image,name='image'),
    url('^$',views.uploaded_photos,name ='uploadedPhotos')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)