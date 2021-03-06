# Generated by Django 3.1.2 on 2020-10-12 15:26

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_auto_20201012_1807'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='categories',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_location',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='image',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_category',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_name',
        ),
        migrations.AddField(
            model_name='image',
            name='categories',
            field=models.ManyToManyField(to='photos.categories'),
        ),
        migrations.AddField(
            model_name='image',
            name='description',
            field=tinymce.models.HTMLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='gallery_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
