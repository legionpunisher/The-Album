from django.db import models

# Create your models here.
class Uploader(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField() 
       
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

class Image(models.Model):
    image=models.ImageField()
    image_name = models.CharField(max_length=30)    
    uploader=models.ForeignKey(Uploader,on_delete=models.CASCADE)
    Description=models.TextField()
    image_location=models.ForeignKey('Location',on_delete=models.CASCADE)
    image_category=models.ForeignKey('Category',on_delete=models.CASCADE)


    def __str__(self):
        return self.image

class Location(models.Model):
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
   