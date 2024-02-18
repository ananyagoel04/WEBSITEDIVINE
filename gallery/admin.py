from django.contrib import admin
from gallery.models import Gallery
from gallery.models import maingallery

class galleryadmin(admin.ModelAdmin):
    list_display=('image_title','imagefilter','image')
    def has_add_permission(self, request):
        # Check the total number of existing entries
        total_entries = Gallery.objects.count()
        
        # Set the maximum number of allowed entries
        max_entries = 6
        
        # Allow adding if the total entries are less than the maximum
        return total_entries < max_entries
class galleryadmin1(admin.ModelAdmin):
    list_display=('image_title1','imagefilter1','image1')

admin.site.register(Gallery,galleryadmin)
admin.site.register(maingallery,galleryadmin1)
# Register your models here.
