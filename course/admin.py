from django.contrib import admin

# Register your models here.
from .models import Course,Chapter,Lecture,Quiz,Question,Assignment

admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Lecture)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Assignment)
