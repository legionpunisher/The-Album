from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def all_photos(request):
    photos=Image.view_photo()
    return render(request,'image.html',{'photos':photos})