from django.conf.urls import url
from . import views

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url('^$',views.uploaded_photos,name ='uploadedPhotos')
]