from django.contrib import admin
from .models import Homeimg, VisionMission, Environment, Teacher, Program, Review

class HomeimgAdmin(admin.ModelAdmin):
    list_display = ('image_title', 'image')
    search_fields = ('image_title',)
    exclude = ('id',)
    
    def has_add_permission(self, request):
        total_entries = Homeimg.objects.count()
        max_entries = 1  # Different limit for Homeimg
        return total_entries < max_entries

class VisionMissionAdmin(admin.ModelAdmin):
    list_display = ('image_title', 'image')
    search_fields = ('image_title',)
    exclude = ('id',)

    def has_add_permission(self, request):
        total_entries = VisionMission.objects.count()
        max_entries = 2  # Different limit for VisionMission
        return total_entries < max_entries

class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('image_title', 'image')
    search_fields = ('image_title',)
    exclude = ('id',)

    def has_add_permission(self, request):
        total_entries = Environment.objects.count()
        max_entries = 2  # Different limit for Environment
        return total_entries < max_entries

class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'image_title', 'image')
    search_fields = ('name', 'designation')
    exclude = ('id',)
    
    def has_add_permission(self, request):
        total_entries = Teacher.objects.count()
        max_entries = 4  # Different limit for Teachers
        return total_entries < max_entries

class ProgramsAdmin(admin.ModelAdmin):
    list_display = ('image_title', 'image')
    search_fields = ('image_title',)
    exclude = ('id',)
    
    def has_add_permission(self, request):
        total_entries = Program.objects.count()
        max_entries = 3  # Different limit for Programs
        return total_entries < max_entries

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars', 'review', 'image_title', 'image')
    search_fields = ('name', 'review')
    exclude = ('id',)
    
    def has_add_permission(self, request):
        total_entries = Review.objects.count()
        max_entries = 4  # Different limit for Reviews
        return total_entries < max_entries

# Register each model with its corresponding admin class
admin.site.register(Homeimg, HomeimgAdmin)
admin.site.register(VisionMission, VisionMissionAdmin)
admin.site.register(Environment, EnvironmentAdmin)
admin.site.register(Teacher, TeachersAdmin)
admin.site.register(Program, ProgramsAdmin)
admin.site.register(Review, ReviewsAdmin)
