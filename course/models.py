from django.db import models
from datetime import datetime
from django.utils import timezone
import math
# Create your models here.
class Course(models.Model):
    course_id= models.AutoField
    course_name=models.CharField(max_length=20)   
    
    def __str__(self):
        return self.course_name

class Chapter(models.Model):
    chapter_id=models.AutoField(primary_key=True)
    chapter_name=models.CharField(max_length=30)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.chapter_name 

class Lecture(models.Model):
    lecture_name=models.CharField(max_length=50)
    ytvideo = models.CharField(max_length=500,blank=True)
    src=models.FileField(upload_to ='course/videos',blank=True)
    chapter=models.ForeignKey(Chapter,on_delete=models.CASCADE)

    def __str__(self):
        return self.lecture_name 

class Quiz(models.Model):
    quiz_name=models.CharField(max_length=100)
    time=models.IntegerField()
    chapter=models.ForeignKey(Chapter,on_delete=models.CASCADE)
    done=models.BooleanField(default=False)

    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    statement=models.CharField(max_length=200)
    correct_ans=models.CharField(max_length=200)
    options=models.CharField(max_length=500)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)

    def splitoptions(self):
        return self.options.split(' ')
    def __str__(self):
        return self.statement

class Assignment(models.Model):
    chapters=models.CharField(max_length=500)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField(auto_now_add=False)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    ass_name=models.CharField(max_length=30)

    def days_left(self):
        return (self.end_date-timezone.now()).days

    def hour_left(self):
        return (math.floor(((self.end_date-timezone.now()).seconds)/3600))
    
    def days_given(self):
        return (self.end_date-self.start_date).days
    
    def notgiven(self):
        return timezone.now()>self.end_date

    def __str__(self):
        return self.ass_name

