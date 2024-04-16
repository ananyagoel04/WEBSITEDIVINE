from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import cloudinary

class about(models.Model):
    pdftitle = models.CharField(max_length=100)    
    pdf = models.FileField(upload_to='about/', null=True, default=None)

    def get_pdf_url(self):
        return self.pdf.url
@receiver(pre_delete, sender=about)
def about_file_cleanup(sender, instance, **kwargs):
    # Check if the instance has an image and it's not the default value
    if instance.pdf and 'default_pdf' not in instance.pdf.name:
        # Extract public_id from Cloudinary URL
        public_id = instance.pdf.name.split('.')[0]
        # Delete the image from Cloudinary
        cloudinary.uploader.destroy(public_id)

@receiver(pre_save, sender=about)
def about_file_update(sender, instance, **kwargs):
    # Check if the instance has an image and it's not the default value
    if instance.pdf and 'default_pdf' not in instance.pdf.name:
        try:
            # Get the existing instance from the database
            old_instance = about.objects.get(pk=instance.pk)
            # Extract public_id from Cloudinary URL
            old_public_id = old_instance.image.pdf.split('.')[0]
            new_public_id = instance.image.pdf.split('.')[0]
            # Compare the old and new images' public_ids
            if old_public_id != new_public_id:
                # Delete the old image from Cloudinary
                cloudinary.uploader.destroy(old_public_id)
        except about.DoesNotExist:
            pass  # Handle the case of a new instance being created



class aboutimg(models.Model):
    image_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="aboutimg/", null=True, default=None)

    def get_image_url(self):
        return self.image.url

@receiver(pre_delete, sender=aboutimg)
def gallery_file_cleanup(sender, instance, **kwargs):
    # Check if the instance has an image and it's not the default value
    if instance.image and 'default_image' not in instance.image.name:
        # Extract public_id from Cloudinary URL
        public_id = instance.image.name.split('.')[0]
        # Delete the image from Cloudinary
        cloudinary.uploader.destroy(public_id)

@receiver(pre_save, sender=aboutimg)
def gallery_file_update(sender, instance, **kwargs):
    # Check if the instance has an image and it's not the default value
    if instance.image and 'default_image' not in instance.image.name:
        try:
            # Get the existing instance from the database
            old_instance = aboutimg.objects.filter(pk=instance.pk).first()
            if old_instance:
                # Extract public_id from Cloudinary URL
                old_public_id = old_instance.image.name.split('.')[0]
                new_public_id = instance.image.name.split('.')[0]
                # Compare the old and new images' public_ids
                if old_public_id != new_public_id:
                    # Delete the old image from Cloudinary
                    cloudinary.uploader.destroy(old_public_id)
        except aboutimg.DoesNotExist:
            pass  # Handle the case of a new instance being created



