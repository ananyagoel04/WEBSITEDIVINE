# Generated by Django 5.0.1 on 2024-02-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_alter_gallery_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image_title',
            field=models.CharField(max_length=10),
        ),
    ]