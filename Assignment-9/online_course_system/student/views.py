from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import CourseSubscription, StudentInfo, Course

# Create your views here.


def info(request):
    if request.user.is_authenticated == True:
        return render(request, "student/info.html")
    return redirect("home")


def index(request):
    return render(request,"student/index.html")


def ChangePassword(request):
    if request.user.is_authenticated == True:
        if request.method == 'POST':
            newpassword = request.POST['newPassword']
            users = User.objects.filter(username=request.user).first()
            users.set_password(newpassword)
            users.save()
            logout(request)
            return redirect("home")
        return render(request, "student/change_password.html")
    return redirect("home")


def unsubscribe(request,slug):
    user = StudentInfo.objects.filter(user=request.user).first()
    course = Course.objects.filter(course_slug=slug).first()
    ucourse = CourseSubscription.objects.filter(student=user)
    contest = {
        "ucourse": ucourse,
    }
    unsubscription_course = CourseSubscription.objects.filter(
        student=StudentInfo.objects.filter(user=request.user).first(),
        course=course).first()
    unsubscription_course.delete()

    return render(request, 'student/user_course.html',contest)


def UserCourse(request):
    if request.user.is_authenticated == True:
        user = StudentInfo.objects.filter(user=request.user).first()
        ucourse = CourseSubscription.objects.filter(student=user)
        contest = {
            "ucourse":ucourse,
        }
        return render(request, "student/user_course.html", contest)
    return redirect("home")


def logout_view(request):
    logout(request)
    return render(request,'dashboard/home.html')

# class Search(ListView):
#     model = Course
#     template_name = 'ecomm/search.html'
#     context_object_name = 'all_search_results'
#
#     def get_queryset(self):
#         result = super(Search, self).get_queryset()
#         query = self.request.GET.get('search')
#         if query:
#             postresult = Course.objects.filter(title__contains=query)
#             result = postresult
#         else:
#             result = None
#         return result

def search(request):
    # if request.method == "POST":
        search_value = request.GET['search']
        course=Course.objects.filter(title__icontains=search_value)
        context={
          'course':course
        }
        return render(request, "course/courses.html", context)
    # return redirect("student/index.html")
