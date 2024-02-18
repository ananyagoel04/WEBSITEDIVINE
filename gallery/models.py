from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import os

class Gallery(models.Model):
    image_title=models.CharField(max_length=10)
    filter = [
        ('Nature', 'Nature'),
        ('Architect', 'Architect'),
        ('Preprimary', 'Preprimary'),
    ]
    imagefilter = models.CharField(
        max_length=20,
        choices=filter,
        default='Nature',  # Set a default value if needed
    )
    image=models.FileField(upload_to="maingallery/", max_length=100, null=True, default=None)
@receiver(pre_delete, sender=Gallery)
def gallery_file_cleanup(sender, instance, **kwargs):
    # Check if the instance has a file and it's not the default value
    if instance.image and instance.image.name != 'maingallery/default_image.jpg':
        # Delete the old file before saving the new one
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(pre_save, sender=Gallery)
def gallery_file_update(sender, instance, **kwargs):
    # Check if the instance has a file and it's not the default value
    if instance.image and instance.image.name != 'maingallery/default_image.jpg':
        try:
            # Get the existing instance from the database
            old_instance = Gallery.objects.get(pk=instance.pk)
            # Compare the old and new file paths
            if old_instance.image.path != instance.image.path:
                # Delete the old file before saving the new one
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        except Gallery.DoesNotExist:
            pass  # Handle the case of a new instance being created

class maingallery(models.Model):
    image_title1=models.CharField(max_length=10)
    filter1 = [
        ('Nature', 'Nature'),
        ('Architect', 'Architect'),
        ('Preprimary', 'Preprimary'),
    ]
    imagefilter1 = models.CharField(
        max_length=20,
        choices=filter1,
        default='Nature',  # Set a default value if needed
    )
    image1=models.FileField(upload_to="maingallerylist/", max_length=100, null=True, default=None)

@receiver(pre_delete, sender=maingallery)
def maingallery_file_cleanup(sender, instance, **kwargs):
    # Check if the instance has a file and it's not the default value
    if instance.image1 and instance.image1.name != 'maingallerylist/default_image.jpg':
        # Delete the old file before saving the new one
        if os.path.isfile(instance.image1.path):
            os.remove(instance.image1.path)
@receiver(pre_save, sender=maingallery)
def maingallery_file_update(sender, instance, **kwargs):
    # Check if the instance has a file and it's not the default value
    if instance.image1 and instance.image1.name != 'maingallerylist/default_image.jpg':
        try:
            # Get the existing instance from the database
            old_instance = maingallery.objects.get(pk=instance.pk)
            # Compare the old and new file paths
            if old_instance.image1.path != instance.image1.path:
                # Delete the old file before saving the new one
                if os.path.isfile(old_instance.image1.path):
                    os.remove(old_instance.image1.path)
        except maingallery.DoesNotExist:
            pass  # Handle the case of a new instance being created
