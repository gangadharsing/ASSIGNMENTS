from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import CourseSubscription, StudentInfo
from course.models import Course


# Create your views here.
def info(request):
    if request.user.is_authenticated == True:
        return render(request, "student/info.html")
    return redirect(request, "home")


def index(request):
    return render(request, "student/index.html")


def change_password(request):
    if request.user.is_authenticated == True:
        if request.method == 'POST':
            newpassword = request.POST['newPassword']
            users = User.objects.filter(username=request.user).first()
            users.set_password(newpassword)
            users.save()
            logout(request)
            return redirect("index")
        return render(request, 'student/change_password.html')
    return render(request, "home")


def user_course(request):
    if request.user.is_authenticated == True:
        user = StudentInfo.objects.filter(username=request.user).first()
        ucourse = CourseSubscription.objects.filter(student=user)
        context = {
            "ucourse": ucourse,
        }
        return render(request, 'student/user_course.html', context)
    return render(request, "index")


def delete(request, ucourse):
    data = get_object_or_404(ucourse=ucourse)
    data.delete()
    return render(request, 'student/user_course.html')


def search_value(request):
    search_post = request.GET['q']
    course = Course.objects.filter(title__icontains=search_post)
    # If not searched, return default posts
    context = {
        'course': course
    }
    return render(request, 'course/courses.html',  context)


def unsubscribe(request,slug):
    user = StudentInfo.objects.filter(username=request.user).first()
    course = Course.objects.filter(course_slug=slug).first()
    ucourse = CourseSubscription.objects.filter(student=user)
    contest = {
        "ucourse": ucourse,
    }
    unsubscription_course = CourseSubscription.objects.filter(
        student=StudentInfo.objects.filter(username=request.user).first(),
        course=course).first()
    unsubscription_course.delete()

    return render(request, 'student/user_course.html',contest)
