from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import os
class about(models.Model):
    image_title=models.CharField(max_length=50)
    imageabout=models.FileField(upload_to="about/", max_length=100, null=True, default=None)
@receiver(pre_save, sender=about)
def about_file_update(sender, instance, **kwargs):
        # Check if the instance has a file and it's not the default value
        if instance.imageabout and instance.imageabout.name != 'about/default_image.jpg':
            try:
                # Get the existing instance from the database
                old_instance = about.objects.get(pk=instance.pk)
                # Compare the old and new file paths
                if old_instance.imageabout.path != instance.imageabout.path:
                    # Delete the old file before saving the new one
                    if os.path.isfile(old_instance.imageabout.path):
                        os.remove(old_instance.imageabout.path)
            except about.DoesNotExist:
                pass  # Handle the case of a new instance being created
# Create your models here.
