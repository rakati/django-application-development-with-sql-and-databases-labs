from django.contrib import admin
from .models import Course, Instructor, Lesson

# Register your models here.


class LessonInline(admin.StackedInline):
    """associate lesson object into Course model managing page"""
    model = Lesson
    extra = 5


class CourseAdmin(admin.ModelAdmin):
    """customize fields included in Course admin page"""
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]


class InstructorAdmin(admin.ModelAdmin):
    """customize fields included in Instructor admin page"""
    fields = ['user', 'full_time']


admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
