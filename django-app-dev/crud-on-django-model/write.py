# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date


def write_instructors():
    # Add instructors
    # Create a user
    user_john = User(first_name='John', last_name='Doe', dob=date(1962, 7, 16))
    user_john.save()
    instructor_john = Instructor(full_time=True, total_learners=30050)
    # Update the user reference of instructor_john to be user_john
    instructor_john.user = user_john
    instructor_john.save()
    
    instructor_yan = Instructor(first_name='Yan', last_name='Luo', dob=date(1962, 7, 16), full_time=True, total_learners=30050)
    instructor_yan.save()

    instructor_joy = Instructor(first_name='Joy', last_name='Li', dob=date(1992, 1, 2), full_time=False, total_learners=10040)
    instructor_joy.save()
    instructor_peter = Instructor(first_name='Peter', last_name='Chen', dob=date(1982, 5, 2), full_time=True, total_learners=2002)
    instructor_peter.save()
    print("Instructor objects all saved... ")

def write_courses():
    # Add Courses
    course_cloud_app = Course(name="Cloud Application Development with Database",
                              description="Develop and deploy application on cloud")
    course_cloud_app.save()
    course_python = Course(name="Introduction to Python",
                           description="Learn core concepts of Python and obtain hands-on "
                                       "experience via a capstone project")
    course_python.save()

    print("Course objects all saved... ")

def write_lessons():
    # Add lessons
    lession1 = Lesson(title='Lesson 1', content="Object-relational mapping project")
    lession1.save()
    lession2 = Lesson(title='Lesson 2', content="Django full stack project")
    lession2.save()
    print("Lesson objects all saved... ")

def clean_data():
    # Delete all data to start from fresh
    Enrollment.objects.all().delete()
    User.objects.all().delete()
    Learner.objects.all().delete()
    Instructor.objects.all().delete()
    Course.objects.all().delete()
    Lesson.objects.all().delete()


def write_learners():
    learner_james = Learner(first_name='James', last_name='Smith', dob=date(1982, 7, 16),
                            occupation='data_scientist',
                            social_link='https://www.linkedin.com/james/')
    learner_james.save()

    learner_mary = Learner(first_name='Mary', last_name='Smith', dob=date(1991, 6, 12),
                           occupation='dba',
                           social_link='https://www.facebook.com/mary/')
    learner_mary.save()

    learner_robert = Learner(first_name='Robert', last_name='Lee', dob=date(1999, 1, 2),
                             occupation='student',
                             social_link='https://www.facebook.com/robert/')
    learner_robert.save()

    learner_david = Learner(first_name='David', last_name='Smith', dob=date(1983, 7, 16),
                            occupation='developer',
                            social_link='https://www.linkedin.com/david/')
    learner_david.save()

    learner_john = Learner(first_name='John', last_name='Smith', dob=date(1986, 3, 16),
                           occupation='developer',
                           social_link='https://www.linkedin.com/john/')
    learner_john.save()

    learner_emily = Learner(first_name='Emily', last_name='Clark', dob=date(1994, 2, 25),
                            occupation='student',
                            social_link='https://www.linkedin.com/emily/')
    learner_emily.save()

    learner_michael = Learner(first_name='Michael', last_name='Brown', dob=date(1990, 11, 5),
                              occupation='developer',
                              social_link='https://www.github.com/michael/')
    learner_michael.save()

    learner_sophia = Learner(first_name='Sophia', last_name='Taylor', dob=date(1997, 8, 15),
                             occupation='data_scientist',
                             social_link='https://www.twitter.com/sophia/')
    learner_sophia.save()

    learner_william = Learner(first_name='William', last_name='Green', dob=date(1988, 12, 10),
                              occupation='dba',
                              social_link='https://www.facebook.com/william/')
    learner_william.save()

    learner_olivia = Learner(first_name='Olivia', last_name='Johnson', dob=date(1996, 4, 18),
                             occupation='student',
                             social_link='https://www.linkedin.com/olivia/')
    learner_olivia.save()

    print("Learner objects all saved... ")

clean_data()
write_courses()
write_instructors()
write_lessons()
write_learners()
