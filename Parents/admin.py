# Parent/admin.py
from django.contrib import admin
from .models import Event, News
from .forms import NewsForm

class EventAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('date', 'heading', 'description', 'image')
    # Optional: Add filtering options
    list_filter = ('date',)
    # Optional: Add search functionality
    search_fields = ('heading', 'description')

class NewsAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('Heading', 'News')
    # Use custom form to include TinyMCE editor
    form = NewsForm
    # Optional: Add search functionality
    search_fields = ('Heading',)

admin.site.register(Event, EventAdmin)
admin.site.register(News, NewsAdmin)
