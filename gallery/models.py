from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import cloudinary
import hashlib


class Gallery(models.Model):
    image_title = models.CharField(max_length=50)
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
    image = models.ImageField(upload_to="maingallery/", null=True, default=None)

    def get_image_url(self):
        return self.image.url

@receiver(pre_delete, sender=Gallery)
def gallery_file_cleanup(sender, instance, **kwargs):
    # Check if the instance has an image and it's not the default value
    if instance.image and 'default_image' not in instance.image.name:
        # Extract public_id from Cloudinary URL
        public_id = instance.image.name.split('.')[0]
        # Delete the image from Cloudinary
        cloudinary.uploader.destroy(public_id)

@receiver(pre_save, sender=Gallery)
def gallery_file_update(sender, instance, **kwargs):
    # Check if the instance has an image and it's not the default value
    if instance.image and 'default_image' not in instance.image.name:
        try:
            # Get the existing instance from the database
            old_instance = Gallery.objects.get(pk=instance.pk)
            # Check if the image has changed by comparing file content
            if old_instance.image != instance.image:
                # Extract public_id from Cloudinary URL
                old_public_id = old_instance.image.name.split('.')[0]
                new_public_id = instance.image.name.split('.')[0]
                # Compare the old and new images' public_ids
                if old_public_id != new_public_id:
                    # Delete the old image from Cloudinary
                    cloudinary.uploader.destroy(old_public_id)
        except Gallery.DoesNotExist:
            pass  # Handle the case of a new instance being created


class maingallery(models.Model):
    image_title1 = models.CharField(max_length=50)
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
    image1 = models.ImageField(upload_to="maingallerylist/", null=True, default=None)

    def get_image_url1(self):
        return self.image1.url

@receiver(pre_delete, sender=maingallery)
def maingallery_file_cleanup(sender, instance, **kwargs):
    # Check if the instance has an image and it's not the default value
    if instance.image1 and 'default_image' not in instance.image1.name:
        # Extract public_id from Cloudinary URL
        public_id = instance.image1.name.split('.')[0]
        # Delete the image from Cloudinary
        cloudinary.uploader.destroy(public_id)

@receiver(pre_save, sender=maingallery)
def maingallery_file_update(sender, instance, **kwargs):
    # Check if the instance has an image and it's not the default value
    if instance.image1 and 'default_image' not in instance.image1.name:
        try:
            # Get the existing instance from the database
            old_instance = maingallery.objects.get(pk=instance.pk)
            # Check if the image has changed by comparing file content
            if old_instance.image1 != instance.image1:
                # Extract public_id from Cloudinary URL
                old_public_id = old_instance.image1.name.split('.')[0]
                new_public_id = instance.image1.name.split('.')[0]
                # Compare the old and new images' public_ids
                if old_public_id != new_public_id:
                    # Delete the old image from Cloudinary
                    cloudinary.uploader.destroy(old_public_id)
        except maingallery.DoesNotExist:
            pass  # Handle the case of a new instance being created