from django.db import models

# Create your models here.
class Uploader(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField() 
    phone_number=models.CharField(max_length=10,blank=True)  
    def __str__(self):
        return self.first_name
    def save_uploader(self):
        self.save()        
    def delete_uploader(self):
        self.delete()
    def display_uploader(self):
        self.display()
    def update_uploader(self):
        self.update()

class Location(models.Model):
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30)    
    uploader=models.ForeignKey(Uploader,on_delete=models.CASCADE)
    Description=models.TextField()
    image_location=models.ForeignKey('Location',on_delete=models.CASCADE)
    image_category=models.ForeignKey('Category',on_delete=models.CASCADE)
    
    @classmethod
    def all_images(self):

        return Image.objects.all()

    @classmethod
    def search_by_category(cls,search_images):
        images = Image.objects.filter(categories__name__icontains=search_images)
        return images

    @classmethod
    def view_location(cls,name):
        location = cls.objects.filter(location=name)
        return location

    @classmethod
    def view_category(cls,cat):
        categories = cls.objects.filter(categories=cat)
        return categories
