from utils.mongodb_utils import get_next_id

from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import cloudinary

class Session(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    session_name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.id == 0:
            self.id = get_next_id('Session')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.session_name

class Class(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, to_field='id')
    class_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.session.session_name} - {self.class_name}'

class Student(models.Model):
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=255)
    TC = models.FileField(upload_to='TC/', null=True, default=None)  # Use FileField

    def __str__(self):
        return f'{self.student_name} ({self.class_obj.class_name})'

@receiver(pre_delete, sender=Student)
def student_file_cleanup(sender, instance, **kwargs):
    if instance.TC and 'default' not in instance.TC.name:
        # Extract public_id from the file's URL or name
        public_id = instance.TC.name.split('.')[0]
        # Delete the file from Cloudinary
        cloudinary.uploader.destroy(public_id)

@receiver(pre_save, sender=Student)
def student_file_update(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Student.objects.get(pk=instance.pk)
            old_public_id = old_instance.TC.name.split('.')[0] if old_instance.TC else None
            new_public_id = instance.TC.name.split('.')[0] if instance.TC else None

            if old_public_id and old_public_id != new_public_id and 'default' not in old_public_id:
                # Delete the old file from Cloudinary
                cloudinary.uploader.destroy(old_public_id)
        except Student.DoesNotExist:
            pass  # Handle the case of a new instance being created
