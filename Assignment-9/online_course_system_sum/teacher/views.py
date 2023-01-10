from django.shortcuts import render, redirect
from course.models import Course, Lecture, Section
from django.db.models import Q
from .models import TeacherInfo, CourseAdded
from student.models import CourseSubscription, StudentInfo


# Create your views here.
def info(request):
    if request.user.is_authenticated == True:
        return render(request, "teacher/info.html")
    return redirect("home")


def index(request):
    return render(request, "teacher/index.html")


def add_course(request):
    context = {
        'title': 'add course'
    }
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        thumbnail_url = request.POST['thumbnail_url']
        course_type = request.POST['course_type']
        course_length = request.POST['course_length']
        # course_slug = request.POST['course_slug']
        course_price = request.POST['course_price']
        new_course = Course(title=title, description=description, thumbnail_url=thumbnail_url, course_type=course_type,
                            course_length=course_length, course_price=course_price)
        new_course.save()
        course = Course.objects.filter(title=title).first()
        teacher = TeacherInfo.objects.filter(username=request.user).first()
        new_sub = CourseAdded(teacher=teacher, course=course)
        new_sub.save()
        return redirect('AddedCourse')
    return render(request, 'teacher/add-course.html', context)


def AddedCourse(request):
    if request.user.is_authenticated == True:
        user1 = TeacherInfo.objects.filter(username=request.user).first()
        tcourse = CourseAdded.objects.filter(teacher=user1)
        contest = {
            "tcourse" : tcourse,
        }
        return render(request, "teacher/course_list.html", contest)
    return redirect("teacher/index.html")


def update_course(request):
    user1 = TeacherInfo.objects.filter(username=request.user).first()
    tcourse = CourseAdded.objects.filter(teacher=user1)
    contest = {
        "tcourse": tcourse,
    }
    # course_id = int(course_id)
    # context = {
    #     "course_id": course_id
    # }

    # try:
    #     course = Course.objects.get(id=course_id)
    # except Course.DoesNotExist:
    #     return redirect('index')
    if request.method == "POST":
        tocheck= request.POST['c_title']
        course = Course.objects.filter(title__icontains=tocheck).first()
        course.title = request.POST['title']
        course.description = request.POST['description']
        course.thumbnail_url = request.POST['thumbnail_url']
        course.course_type = request.POST['course_type']
        course.course_length = request.POST['course_length']
        # course_slug = request.POST['course_slug']
        course.course_price = request.POST['course_price']
        course.save()
        return redirect('AddedCourse')
    return render(request, 'teacher/update.html', contest)


def updatecourse(request):
    course = Course.objects.all()
    context = {
        "course": course
    }
    return render(request, 'teacher/update.html', context)


def delete_course(request):
    user1 = TeacherInfo.objects.filter(username=request.user).first()
    tcourse = CourseAdded.objects.filter(teacher=user1)
    context = {
        "tcourse": tcourse,
    }
    return render(request, "teacher/delete.html", context)


def delete_course1(request, course_id):
    course_id = int(course_id)
    try:
        course = Course.objects.filter(id=course_id)
    except Course.DoesNotExist:
        return redirect('index')
    course.delete()
    return render(request, 'teacher/delete.html')


def deletecourse(request):
    if request.method == "POST":
        title= request.POST['title']
        description = request.POST['description']
        thumbnail_url = request.POST['thumbnail_url']
        course_type = request.POST['course_type']
        course_length = request.POST['course_length']
        course_price = request.POST['course_price']
        new_course = Course(title=title, description=description, thumbnail_url=thumbnail_url, course_type=course_type,
                            course_length=course_length, course_price=course_price)
        new_course.save()
    return render(request, 'teacher/delete.html')


def search_value(request):
    search_post = request.GET['q']
    course = Course.objects.filter(title__icontains=search_post)
    # If not searched, return default posts
    context = {
        'course': course
    }
    return render(request, 'course/courses.html',  context)


def course_list(request):
    # course = Course.objects.all()
    return redirect('AddedCourse')


def course_detail(request, slug):
    if not Course.objects.filter(course_slug=slug).exists():
        return render(request, '404.html')
    else:
        course = Course.objects.filter(course_slug=slug).first()
        section = Section.objects.filter(course=course)
        lecture = Lecture.objects.filter(course=course)
        if request.user.is_authenticated == True:
            subscription_course = CourseSubscription.objects.filter(student=StudentInfo.objects.filter
            (username=request.user).first(), course=course).first()
        else:
            subscription_course = None
        context = {
            "course": course,
            "section": section,
            "lecture": lecture,
            "subscription_course": subscription_course,
        }
        return render(request, 'course/course_detail.html', context)




