from django.contrib.auth import login, authenticate, logout
from user.models import User
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import OTPLog, Profile
from .email import email_message
import random
from student.models import StudentInfo
from teacher.models import TeacherInfo


def signin(request):
    context = {
        'title': 'Sign In'
    }
    if request.method == "POST":
        if User.objects.filter(email=request.POST.get('email')).exists():
            request.session['email'] = request.POST.get('email')
            request.session['password'] = request.POST.get('password')
            request.session['usertype'] = request.POST.get('usertype')
            try:
                otp = OTPLog.objects.get(email=request.POST.get('email')).otp
            except:
                otp = random.randint(100000, 999999)
                OTPLog.objects.create(email=request.POST.get('email'), otp=otp).save()

            message = 'Your OTP is: ' + str(otp)
            email_message(request.POST.get('email'), 'Registration OTP', message)

            user = authenticate(request, username=request.session['email'], password=request.session['password'])

            if user is not None:
                login(request, user)
                return redirect("login/otp")
            else:
                context['login_error'] = "Invalid credentials!"
    return render(request, 'user/login.html', context)


def signup(request):
    context = {
        'title': 'Sign Up',
        'reg_errors': [],
    }
    if request.method == "POST":
        if request.POST.get('password1') == request.POST.get('password2'):
            if User.objects.filter(email=request.POST.get('email')).exists():
                context["reg_errors"].append("Email already in use!")

            else:
                request.session['username'] = request.POST.get('username')
                request.session['f_name'] = request.POST.get('f_name')
                request.session['l_name'] = request.POST.get('l_name')
                request.session['email'] = request.POST.get('email')
                request.session['password'] = request.POST.get('password1')
                request.session['usertype'] = request.POST['usertype']
                request.session['mobile_no'] = request.POST['mobile_no'],
                request.session['address'] = request.POST['address'],

                try:
                    otp = OTPLog.objects.get(email=request.POST.get('email')).otp
                except:
                    otp = random.randint(100000, 999999)
                    OTPLog.objects.create(email=request.POST.get('email'), otp=otp).save()

                message = 'Your OTP is: ' + str(otp)
                email_message(request.POST.get('email'), 'Registration OTP', message)

                return redirect("signup/otp")
        else:
            context["reg_errors"].append("Passwords don't match!")
    return render(request, 'user/register.html', context)


def reg_otp_view(request):
    context = {
        'title': 'OTP Verification',
        'email': request.session['email'],
    }

    # if request.POST == "GET":
    #     print("Resend OTP")

    print(OTPLog.objects.get(email=request.session['email']).otp)
    if request.method == "POST":
        otp = OTPLog.objects.get(email=request.session['email'])
        if int(request.POST.get('otp')) == int(otp.otp):
            # username = request.session['email'],
            # first_name=request.session['f_name'],
            # last_name=request.session['l_name'],
            # email=request.session['email'],
            # password=request.session['password']
            # user = User(username=request.session['email'],first_name=request.session['f_name'],last_name=request.session['l_name'],email=request.session['email'],password=request.session['password'])
            # User.objects.create_user(user)
            User.objects.create_user(
                username=request.session['username'],
                first_name=request.session['f_name'],
                last_name=request.session['l_name'],
                email=request.session['email'],
                password=request.session['password']
            )
            user = User.objects.get(username=request.session['username'])
            usertype = request.session['usertype'],
            email = request.session['email'],
            mobile_no = request.session['mobile_no'],
            # dob = request.session['dob'],
            address = request.session['address'],
            pro = Profile(user=user, usertype=request.session['usertype'], email=request.session['email'], mobile_no=request.session['mobile_no'], address=request.session['address'])
            pro.save()
            if request.session['usertype'] == 'STUDENT':
                student = StudentInfo(user=user,email_id=request.session['email'], mobile_no=request.session['mobile_no'], address=request.session['address'])
                student.save()
                user = authenticate(request, username=request.session['email'], password=request.session['password'])
                if user is not None:
                    login(request, user)
                    return redirect('/student/index')
            elif request.session['usertype'] == 'TEACHER':
                teacher = TeacherInfo(user=user, email_id=request.session['email'], mobile_no=request.session['mobile_no'], address=request.session['address'])
                teacher.save()
                user = authenticate(request, username=request.session['email'], password=request.session['password'])
                if user is not None:
                    login(request, user)
                    return redirect('/teacher/index')
            # if user is not None:
            #     login(request, user)
            #     if usertype == 'TEACHER':
            #         return redirect('/teacher/index')
            #     elif usertype == 'STUDENT':
            #         return redirect('/student/index')
            #     else:
            #         return ('/teacher/addcourse')
            else:
                 context['error'] = "Invalid credentials"
        else:
            context['error'] = "Wrong OTP"
    return render(request, 'user/otp.html', context)


def login_otp_view(request):
    context = {
        'title': 'OTP Verification',
        'email': request.session['email'],
        'usertype': request.session['usertype']
    }

    if request.POST == "GET":
        print("Resend OTP")

    print(OTPLog.objects.get(email=request.session['email']).otp)
    if request.method == "POST":
        request.session['usertype']=request.POST.get('user_type')
        otp = OTPLog.objects.get(email=request.session['email'])
        prof=Profile.objects.get(email=request.session['email'])
        if int(request.POST.get('otp')) == int(otp.otp):
            if prof.usertype == 'TEACHER':
                return redirect('/teacher/index')
            elif prof.usertype == 'STUDENT':
                return redirect('/student/index')
                # return redirect('user_selection')
        else:
            context['error'] = "Wrong OTP"
    return render(request, 'user/otp.html',context)


def logout_view(request):
    logout(request)
    return render(request,'dashboard/home.html')


# def user_selection(request):
#     if request.method == "GET":
#         if (request.GET.get('user_type')) ==('teacher'):
#             return redirect('teacher/index')
#         elif (request.GET.get('user_type'))==('student'):
#             return redirect('student/index')
#         else:
#             return render(request,'login.html')
#     return render(request,'otp.html')