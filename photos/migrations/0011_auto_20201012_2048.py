# Generated by Django 3.1.2 on 2020-10-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0010_auto_20201012_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='gallery_image',
            field=models.ImageField(upload_to=''),
        ),
    ]