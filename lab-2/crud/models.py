from django.db import models
from django.utils.timezone import now

# User Model
class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='John')
    last_name = models.CharField(null=False, max_length=30, default='Doe')
    email = models.EmailField(null=False)
    dob = models.DateField(null=True)

    # Create a toString method for object string representation
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


# Instructor model
class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    # Create a toString method for object string representation
    def __str__(self) -> str:
        return "First name: " + self.first_name + ", " + \
               "Last name: " + self.last_name +  ", " + \
               "Is full time: " + str(self.full_time) + ", " + \
               "Total learners: " + str(self.total_learners)

# Learner model
class Learner(User):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    # Occupation char field defined enumeration choices
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    )
    # Social link URL field
    social_link = models.URLField(max_length=200)

    def __str__(self):
        return "First name: " + self.first_name + ", " + \
               "Last name: " + self.last_name +  ", " + \
               "Occupation: " + self.occupation

# Enrollment model as a lookup table with additional enrollment info
class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor'),
    ]
    # Add learner foreign key
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    # Add course foreign key
    course = models.models.ForeignKey(Learner, on_delete=models.CASCADE)
    # Enrollment date
    date_enrolled = models.DateField(default=now)
    # Enrollment mode
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)


# Course model
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)
    # Many-To-Many relationship with Instructor
    instructors = models.ManyToManyField(Instructor)
    # Many-To-Many relationship with Learner via Enrollment
    instructors = models.ManyToManyField(Learner, through='Enrollment')

    # Create a toString method for object string representation
    def __str__(self) -> str:
        return "Name: " + self.name + ", " + \
                "Description: " + self.description

# Lesson model
class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()
