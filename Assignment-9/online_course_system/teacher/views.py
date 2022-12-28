from django.template import RequestContext
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from course.models import Course
from django.contrib.auth.models import User
from .forms import CourseCreate
from user import views
from .models import TeacherInfo,CourseAdded

# Create your views here.
def logout_view(request):
    logout(request)
    return render(request,'dashboard/home.html')



def index(request):
    return render(request,"teacher/index.html")


def addcourse(request):
    context = {
        'title': 'add course'
    }

    if request.method == "POST":
        title= request.POST['title']
        description = request.POST['description']
        thumbnail_url = request.POST['thumbnail_url']
        course_type = request.POST['course_type']
        course_length = request.POST['course_length']
        course_price = request.POST['course_price']
        new_course = Course(title=title, description=description, thumbnail_url=thumbnail_url, course_type=course_type,course_length=course_length,course_price=course_price)
        new_course.save()
        course=Course.objects.filter(title=title).first()
        teacher = TeacherInfo.objects.filter(username=request.user).first()
        new_sub = CourseAdded(teacher=teacher, course=course)
        new_sub.save()
        return redirect('AddedCourse')
    return render(request,'teacher/addcourse.html',context)

def AddedCourse(request):
    if request.user.is_authenticated == True:
        user1 = TeacherInfo.objects.filter(username=request.user).first()
        tcourse = CourseAdded.objects.filter(teacher=user1)
        contest = {
            "tcourse":tcourse,
        }
        return render(request, "teacher/courselist.html", contest)
    return redirect("teacher/index.html")

def updatecourse(request,c_title):

    if request.method == "POST":
        course = Course.objects.Get(title=c_title)
        course.title= request.POST['title']
        course.description = request.POST['description']
        course.thumbnail_url = request.POST['thumbnail_url']
        course.course_type = request.POST['course_type']
        course.course_length = request.POST['course_length']
        course.course_price = request.POST['course_price']
        #course1=Course(course)

        course.save()

        for object in course:
            object.save()
    else:
        course=Course.objects.all()
        context ={
            "course":course
        }
        return render(request,'teacher/updatecourse.html',context)

def courselist(request):
    # course = Course.objects.all()
    return redirect('AddedCourse')
    # return render(request, 'teacher/courselist.html', {'course': course})

def update_course(request, course_id):
    tcourse=Course.objects.all()
    context1={
        "tcourse":tcourse
    }
    course_id = int(course_id)
    context={
        "course_id":course_id
    }

    try:
        course = Course.objects.get(id = course_id)
    except Course.DoesNotExist:
        return redirect('index')
    if request.method == "POST":
        # course.id = request.POST['cid']
        course.title = request.POST['title']
        course.description = request.POST['description']
        course.thumbnail_url = request.POST['thumbnail_url']
        course.course_type = request.POST['course_type']
        course.course_length = request.POST['course_length']
        course.course_price = request.POST['course_price']
        # course_form = Course(course)
        course.save()
        return redirect('AddedCourse')
        # return render(request,'teacher/courselist.html',context1)
    return render(request,'teacher/updatecourse.html', context)

def delete_course(request,course_id):
    course_id = int(course_id)
    try:
        course = Course.objects.get(id = course_id)
    except Course.DoesNotExist:
        return redirect('index')
    course.delete()
    return render(request,'teacher/courselist.html')


def updatecourse(request):

        course=Course.objects.all()
        context ={
            "course":course
        }
        return render(request,'teacher/updatecourse.html',context)


def deletecourse(request):
    if request.method == "POST":
        title= request.POST['title']
        description = request.POST['description']
        thumbnail_url = request.POST['thumbnail_url']
        course_type = request.POST['course_type']
        course_length = request.POST['course_length']
        course_price = request.POST['course_price']
        new_course = Course(title=title, description=description, thumbnail_url=thumbnail_url, course_type=course_type, course_length=course_length,
                           course_price=course_price)
        new_course.save()
    return render(request,'templates/teacher/deletecourse.html')

