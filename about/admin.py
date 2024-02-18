from django.contrib import admin
from about.models import about

class aboutadmin(admin.ModelAdmin):
    list_displayabout=('image_title','imageabout')

admin.site.register(about,aboutadmin)


# Register your models here.
