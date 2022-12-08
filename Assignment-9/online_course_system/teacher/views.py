from django.contrib.auth import logout
from django.shortcuts import render
from course.models import Course
from user import views


# Create your views here.
def logout_view(request):
    logout(request)
    return render(request,'dashboard/home.html')



def index(request):
    return render(request,"teacher/index.html")


def addcourse(request):
    if request.method == "POST":
        title= request.POST['title']
        description = request.POST['description']
        thumbnail_url = request.POST['thumbnail_url']
        course_type = request.POST['course_type']
        course_length = request.POST['course_length']
        course_slug = request.POST['course_slug']
        course_price = request.POST['course_price']
        new_course = Course(title=title, description=description, thumbnail_url=thumbnail_url, course_type=course_type, course_length=course_length,
                          course_slug=course_slug, course_price=course_price)
        new_course.save()
    return render(request,'teacher/addcourse.html')


def updatecourse(request):
    if request.method == "POST":
        title= request.POST['title']
        description = request.POST['description']
        thumbnail_url = request.POST['thumbnail_url']
        course_type = request.POST['course_type']
        course_length = request.POST['course_length']
        course_slug = request.POST['course_slug']
        course_price = request.POST['course_price']
        new_course = Course(title=title, description=description, thumbnail_url=thumbnail_url, course_type=course_type, course_length=course_length,
                          course_slug=course_slug, course_price=course_price)
        new_course.save()
    return render(request,'templates/teacher/updatecourse.html')


def deletecourse(request):
    if request.method == "POST":
        title= request.POST['title']
        description = request.POST['description']
        thumbnail_url = request.POST['thumbnail_url']
        course_type = request.POST['course_type']
        course_length = request.POST['course_length']
        course_slug = request.POST['course_slug']
        course_price = request.POST['course_price']
        new_course = Course(title=title, description=description, thumbnail_url=thumbnail_url, course_type=course_type, course_length=course_length,
                          course_slug=course_slug, course_price=course_price)
        new_course.save()
    return render(request,'templates/teacher/deletecourse.html')

