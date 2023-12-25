# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from related_objects.models import *
from datetime import date


# Course has intructors refence field so can be used directly via forward access
a_yan_courses = Course.objects.filter(instructors__first_name='Yan')
print("1.a Get courses taught by Instructor `Yan`, forward")
print(a_yan_courses)

print()

b_yan_courses = Instructor.objects.get(first_name='Yan').courses_set.all()
print("1.b Get courses taught by Instructor `Yan`, forward")
print(b_yan_courses)



