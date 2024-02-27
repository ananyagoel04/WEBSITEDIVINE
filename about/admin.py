# admin.py

from django.contrib import admin
from about.models import about

class aboutad(admin.ModelAdmin):
    list_display=('pdftitle','pdf')


admin.site.register(about,aboutad)
