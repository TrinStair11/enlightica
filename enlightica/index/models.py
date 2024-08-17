from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    duration = models.IntegerField()
    image = models.ImageField(upload_to='static/course_images/', blank=True)
    instructor = models.CharField(max_length=64, default='Instructor')
    start_date = models.DateField(default='2020-01-01')
    enrollment_deadline = models.DateField(default='2020-01-01')
    related_courses = models.ManyToManyField('self', blank=True)
    

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=256)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    video = models.FileField(upload_to='static/lesson_videos/', blank=True)
    order = models.IntegerField()
    
    

    def __str__(self):
        return self.name