from django.db import models
from django.utils.timezone import now

# User model
class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=False, max_length=30, default='doe')
    dob = models.DateField(null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

# Instructor
class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    def __str__(self):
        return f"First name: {self.first_name}, Last name: {self.last_name}, Is full time: {self.full_time}, Total Learners: {self.total_learners}"

# Learner
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
    occupation = models.CharField(max_length=20, choices=OCCUPATION_CHOICES, default=STUDENT)
    social_link = models.URLField(max_length=200)

    def __str__(self):
        return f"First name: {self.first_name}, Last name: {self.last_name}, DOB: {self.dob}, Occupation: {self.occupation}, Social Link: {self.social_link}"

# Course
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)
    instructors = models.ManyToManyField(Instructor)
    learners = models.ManyToManyField(Learner, through='Enrollment')

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"

# Lesson
class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()

# Enrollment 
class Enrollment(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(default=now)
    mode = models.CharField(max_length=10, choices=[('audit', 'Audit'), ('honor', 'Honor'), ('beta', 'Beta')], default='audit')
    rating = models.FloatField(default=5.0)
