# Generated by Django 3.1.2 on 2020-10-12 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_auto_20201012_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='gallery_image',
            field=models.ImageField(blank=True, upload_to='album/'),
        ),
    ]