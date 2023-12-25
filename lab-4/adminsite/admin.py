from django.contrib import admin
from .models import Course, Instructor, Lesson

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    """The class is responsible for customization of field in admin page
    for the Course model"""
    fields = ['pub_date', 'name', 'description']


admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor)
