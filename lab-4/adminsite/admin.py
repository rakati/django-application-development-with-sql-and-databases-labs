from django.contrib import admin
from .models import Course, Instructor, Lesson

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    """customize fields included in Course admin page"""
    fields = ['pub_date', 'name', 'description']


class InstructorAdmin(admin.ModelAdmin):
    """customize fields included in Instructor admin page"""
    fields = ['user', 'full_time']


admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
