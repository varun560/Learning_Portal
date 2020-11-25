from django.urls import path
from . import views

urlpatterns = [
    path("", views.courselist, name="CoursesList"),
    path("courses/",views.courselist, name="CoursesList"),
    path("courseView/<int:pid>",views.CourseView,name="CourseView"),
    path("courseView/<int:cid>/<int:lid>",views.LectureView,name="LectureView"),
    path("courseView/<int:cid>/quiz/<int:qid>",views.QuizView,name="QuizView"),
    path("courseView/<int:cid>/quiz/<int:qid>/result/",views.QuizResult,name="QuizResult"),
    path("assignments/",views.AssignmentView,name="AssignmentView"),
    path("assignments/<int:aid>",views.AssignmentLoad,name="AssignmentLoad")
]   