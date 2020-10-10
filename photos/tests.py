from django.test import TestCase
from .models import Uploader,Image,Category,Location
# Create your tests here.
class UploaderTestClass(TestCase):
    def setUp(self):
        self.john=Uploader(first_name='john',last_name='lee',email='123@gmail.com')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.john,Uploader))
# Testing Save Method
    def test_save_method(self):
        self.john.save_uploader()
        uploader = Uploader.objects.all()
        self.assertTrue(len(uploader) > 0)
# Testing Delete Method
    def test_delete_method(self):
        self.john.save_uploader()
        uploader = Uploader.objects.all()
        self.assertTrue(len(uploader) > 0)
# Testing display Method
    def test_display_method(self):
        self.john.save_uploader()
        uploader = Uploader.objects.all()
        self.assertTrue(len(uploader) > 0)
# Testing updating Method
    def test_updating_method(self):
        self.john.save_uploader()
        uploader = Uploader.objects.all()
        self.assertTrue(len(uploader) > 0)

