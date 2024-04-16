# admin.py

from django.contrib import admin
from about.models import about
from about.models import aboutimg


class aboutad(admin.ModelAdmin):
    list_display=('pdftitle','pdf')

class abouti(admin.ModelAdmin):
    list_display=('image_title','image')
    def has_add_permission(self, request):
        # Check the total number of existing entries
        total_entries = aboutimg.objects.count()
        
        # Set the maximum number of allowed entries
        max_entries = 6
        
        # Allow adding if the total entries are less than the maximum
        return total_entries < max_entries


admin.site.register(about,aboutad)
admin.site.register(aboutimg,abouti)
