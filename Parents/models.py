# myapp/models.py
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import cloudinary.uploader
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE

class Event(models.Model):
    image = models.ImageField(upload_to="events/", null=True, default=None)
    date = models.DateField()
    heading = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.heading

@receiver(pre_delete, sender=Event)
def event_file_cleanup(sender, instance, **kwargs):
    if instance.image and 'default_image' not in instance.image.name:
        try:
            # Extract public_id from the image URL
            public_id = instance.image.name.split('.')[0]
            # Delete the image from Cloudinary
            cloudinary.uploader.destroy(public_id)
        except Exception as e:
            print(f"Failed to delete image from Cloudinary for Event ID {instance.pk}: {e}")

@receiver(pre_save, sender=Event)
def event_file_update(sender, instance, **kwargs):
    if instance.image and 'default_image' not in instance.image.name:
        try:
            if instance.pk:
                # Get the existing instance from the database
                old_instance = Event.objects.get(pk=instance.pk)
                # Extract public_ids from the old and new images
                old_public_id = old_instance.image.name.split('.')[0]
                new_public_id = instance.image.name.split('.')[0]
                # Compare the old and new images' public_ids
                if old_public_id != new_public_id:
                    # Delete the old image from Cloudinary
                    cloudinary.uploader.destroy(old_public_id)
        except Event.DoesNotExist:
            # Handle the case of a new instance being created
            pass
        except Exception as e:
            print(f"Failed to update image on Cloudinary for Event ID {instance.pk}: {e}")




class News(models.Model):
    Heading = models.CharField(max_length=100)
    News = HTMLField()