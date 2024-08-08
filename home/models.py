from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import cloudinary.uploader
from utils.mongodb_utils import get_next_id


class Homeimg(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    image_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="homeimg/home/", null=True, default=None)

    def save(self, *args, **kwargs):
        if self.id == 0:
            self.id = get_next_id('home')
        super().save(*args, **kwargs)

    def get_image_url(self):
        return self.image.url

class VisionMission(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    image_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="homeimg/vision/", null=True, default=None)

    def save(self, *args, **kwargs):
        if self.id == 0:
            self.id = get_next_id('home')
        super().save(*args, **kwargs)

    def get_image_url(self):
        return self.image.url

class Environment(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    image_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="homeimg/environment/", null=True, default=None)

    def save(self, *args, **kwargs):
        if self.id == 0:
            self.id = get_next_id('home')
        super().save(*args, **kwargs)

    def get_image_url(self):
        return self.image.url

class Teacher(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    image_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="homeimg/teachers/", null=True, default=None)

    def save(self, *args, **kwargs):
        if self.id == 0:
            self.id = get_next_id('home')
        super().save(*args, **kwargs)

    def get_image_url(self):
        return self.image.url

class Program(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    image_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="homeimg/programs/", null=True, default=None)

    def save(self, *args, **kwargs):
        if self.id == 0:
            self.id = get_next_id('home')
        super().save(*args, **kwargs)

    def get_image_url(self):
        return self.image.url

class Review(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=50)
    stars = models.IntegerField()
    review = models.CharField(max_length=225)  # Changed 'reviews' to 'review' for clarity
    image_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="homeimg/reviews/", null=True, default=None)

    def save(self, *args, **kwargs):
        if self.id == 0:
            self.id = get_next_id('home')
        super().save(*args, **kwargs)
        
    def get_image_url(self):
        return self.image.url

def cleanup_image(sender, instance, **kwargs):
    if instance.image and 'default_image' not in instance.image.name:
        public_id = instance.image.name.split('.')[0]
        cloudinary.uploader.destroy(public_id)

def update_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image and 'default_image' not in old_instance.image.name:
                old_public_id = old_instance.image.name.split('.')[0]
                new_public_id = instance.image.name.split('.')[0]
                if old_public_id != new_public_id:
                    cloudinary.uploader.destroy(old_public_id)
        except sender.DoesNotExist:
            pass

# Register signal handlers for all models
models = [Homeimg, VisionMission, Environment, Teacher, Program, Review]
for model in models:
    pre_delete.connect(cleanup_image, sender=model)
    pre_save.connect(update_image, sender=model)
