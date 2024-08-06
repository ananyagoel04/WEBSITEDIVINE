from django.contrib import admin
from .models import Session, Class, Student

class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_name',)
    exclude = ('id',)

class ClassAdmin(admin.ModelAdmin):
    list_display = ('session', 'class_name')
    search_fields = ('session__session_name', 'class_name')
    list_filter = ('session',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'class_obj', 'TC')
    search_fields = ('student_name',)
    list_filter = ('class_obj',)

admin.site.register(Session, SessionAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Student, StudentAdmin)
