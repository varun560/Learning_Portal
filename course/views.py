from django.shortcuts import render
from django.shortcuts import redirect
from .models import Course,Chapter,Lecture,Question,Quiz,Assignment

# Create your views here.
from django.http import HttpResponse

def courselist(request):
    courses=Course.objects.all()
    params={'clist':courses}
    return render(request, 'course/list.html',params)

def CourseView(request,pid):
    course=Course.objects.filter(id=pid)
    chapter=Chapter.objects.filter(course=course[0])
    lectures={}
    quizzes={}
    for c in chapter:
        for l in Lecture.objects.filter(chapter=c):
            lectures[c.chapter_name]=lectures.get(c.chapter_name,[])
            lectures[c.chapter_name].append(l)
    for c in chapter:
        for q in Quiz.objects.filter(chapter=c):
            quizzes[c.chapter_name]=quizzes.get(c.chapter_name,[])
            quizzes[c.chapter_name].append(q)
    return render(request,'course/courseView.html',{'course':course[0],'chapter':chapter,'lectures':lectures,'quizzes':quizzes})

def LectureView(request,cid,lid):
    chapter=Chapter.objects.filter(chapter_id=cid)
    lecture=Lecture.objects.filter(id=lid)
    return render(request,'course/lectureView.html',{'chapter':chapter[0],'lecture':lecture[0]})

def QuizView(request,cid,qid):
    chapter=Chapter.objects.filter(chapter_id=cid)
    quiz=Quiz.objects.filter(id=qid)
    questions=[]
    for q in Question.objects.filter(quiz=quiz[0]):
        questions.append(q)
    return render(request,'course/quizView.html',{'chapter':chapter[0],'questions':questions,'quiz':quiz[0]})

def QuizResult(request,cid,qid):
    if request.method=="POST":
        quiz=Quiz.objects.filter(id=qid)
        correct=0
        incorrect=0
        for q in Question.objects.filter(quiz=quiz[0]):
            if q.correct_ans==request.POST.get(str(q.id)):
                correct=correct+1
            else:
                incorrect=incorrect+1
        total=correct+incorrect
    chapter=Chapter.objects.filter(chapter_id=cid)
    course=chapter[0].course
    return render(request,'course/quizResult.html',{'quiz':quiz[0],'correct':correct,'total':total,'course':course})

def AssignmentView(request):
    assignments={}
    for a in Assignment.objects.all():
        assignments[a.course.course_name]=assignments.get(a.course.course_name,[])
        assignments[a.course.course_name].append(a)
    return render(request, 'course/Assignments.html',{'assignments':assignments})

def AssignmentLoad(request,aid):
    assignment=Assignment.objects.filter(id=aid)
    chapters=assignment[0].chapters.split(',')
    for i in range(len(chapters)):
        chapters[i]=Chapter.objects.filter(chapter_name=chapters[i])[0]
    lectures={}
    quizzes={}
    for c in chapters:
        for l in Lecture.objects.filter(chapter=c):
            lectures[c.chapter_name]=lectures.get(c.chapter_name,[])
            lectures[c.chapter_name].append(l)
    for c in chapters:
        for q in Quiz.objects.filter(chapter=c):
            quizzes[c.chapter_name]=quizzes.get(c.chapter_name,[])
            quizzes[c.chapter_name].append(q)
        return render(request,'course/AssignmentLoad.html',{'assignment':assignment[0],'chapters':chapters,'lectures':lectures,'quizzes':quizzes})

