from django.shortcuts import render, redirect
from .models import Course, Lecture, Section, LectureComment
from student.models import CourseSubscription, StudentInfo, PaymentProcess
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.conf import settings
from paypal.standard.ipn.signals import valid_ipn_received
from django.urls import reverse
from decimal import Decimal
from django.dispatch import receiver
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import get_list_or_404, get_object_or_404
from paypalcheckoutsdk.orders import OrdersGetRequest
import json
import stripe
from .paypal import PayPalClient

# Create your views here.
def courses(request):
    course = Course.objects.all()
    context = {
        "course": course
    }
    return render(request, 'course/courses.html', context)


def course_detail(request, slug):
    if not Course.objects.filter(course_slug=slug).exists():
        return render(request, '404.html')
    else:
        course = Course.objects.filter(course_slug=slug).first()
        section = Section.objects.filter(course=course)
        lecture = Lecture.objects.filter(course=course)
        if request.user.is_authenticated == True:
            subscription_course = CourseSubscription.objects.filter(student=StudentInfo.objects.filter(user=request.user).first(),
            course=course).first()
        else:
            subscription_course = None
        context = {
            "course":course,
            "section":section,
            "lecture":lecture,
            "subscription_course":subscription_course,
        }
        return render(request, 'course/course_detail.html', context)


def lecture_detail(request, slug, lecture_slug):
    if not Course.objects.filter(course_slug=slug).exists() or not Lecture.objects.filter(lecture_slug=lecture_slug).exists():
        return render(request, '404.html')
    else:
        course = Course.objects.filter(course_slug=slug).first()
        section = Section.objects.filter(course=course)
        lecture = Lecture.objects.filter(course=course)
        video = Lecture.objects.filter(lecture_slug=lecture_slug).first()
        Lecture_Comment = LectureComment.objects.filter(lecture=video)

        context ={
            "course":course,
            "section":section,
            "lecture":lecture,
            "video":video,
            "lecture_comment":Lecture_Comment,
        }
        return render(request, 'course/lecture.html', context)

def pricing(request):
    course = Course.objects.filter(course_type="PAID")
    context = {
        "course": course
    }
    return render(request, 'course/pricing.html', context)


@receiver(valid_ipn_received)
def paypal_ipn(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        course = get_object_or_404(Course, id=ipn.invoice)

        if course.course_price == ipn.mc_gross:
            # mark the order as paid
            student = StudentInfo.objects.filter(id=ipn.student)
            new_sub = CourseSubscription(student=student, course=course, payment_id="FREE", order_id="FREE")
            new_sub.save()
            return redirect('UserCourse')


def videoComment(request):
    if request.user.is_authenticated == True:
        if request.method == 'POST':
            comment = request.POST['comment']
            lecture_id = request.POST['lecture_id']
            video = Lecture.objects.filter(id= lecture_id).first()
            new_comment = LectureComment(comment=comment, user=request.user, lecture=video)
            new_comment.save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect('home')


def Checkout(request, slug):
    if not Course.objects.filter(course_slug = slug).exists():
        return render(request, '404.html')
    else:
        if request.user.is_authenticated == True:
            course = Course.objects.filter(course_slug = slug).first()
            # if course.course_price == 0:
            context = {
                "course": course,
                "stripe_publishable_key": settings.STRIPE_API_KEY_PUBLISHABLE
            }
            # else:
            #     return redirect('process_payment')
                # with open("secret key.json",'r') as secret:
                #     key = json.load(secret)['razorpay']
                #  student = StudentInfo.objects.filter(username=request.user).first()
                # client = razorpay.Client(auth=(key['key id'],key['key secret']))
                # payment_id = client.order.create({'amount':course.course_price*100, 'currency':'INR','payment_capture':'1'})
                # new_payment = PaymentProcess(student=student, course=course, order_id=payment_id['id'])
                # new_payment.save()
                # context = {
                #     "course":course,
                #     # "payment":payment_id,
                #     "student":student,
                #     # "key":key['key id'],
                # }

            return render(request, 'course/checkout.html', context)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def process_payment(request):
    PPClient = PayPalClient()

    body = json.loads(request.body)
    data = body["orderID"]
    # user_id = request.user.id

    requestorder = OrdersGetRequest(data)
    response = PPClient.client.execute(requestorder)

    id = response.result.purchase_units[0].custom_id

    course=Course.objects.filter(pk=id).first()
    student=StudentInfo.objects.filter(user=request.user).first()

    new_sub = CourseSubscription(student=student, course=course, payment_id="FREE", order_id="FREE")
    new_sub.save()
    # for item in basket:
    #     OrderItem.objects.create(order_id=order_id, product=item["product"], price=item["price"], quantity=item["qty"])

    return JsonResponse("Payment completed!", safe=False)




def FreeCheckout(request, slug):
    course = Course.objects.filter(course_slug=slug).first()
    if course.course_type == "FREE":
        student = StudentInfo.objects.filter(user=request.user).first()
        new_sub = CourseSubscription(student=student, course=course, payment_id="FREE", order_id="FREE")
        new_sub.save()
        return redirect('UserCourse')
    else:
        return redirect('home')


@csrf_exempt
def payment_done(request):
    user = StudentInfo.objects.filter(user=request.user).first()
    ucourse = CourseSubscription.objects.filter(student=user)
    contest = {
        "ucourse": ucourse,
    }
    return render(request, "student/user_course.html", contest)
    # return render(request, 'payment/payment_done.html')


@csrf_exempt
def payment_canceled(request):

    return render(request, 'payment/payment_cancelled.html')


@csrf_exempt
def create_checkout_session(request, id):

    # request_data = json.loads(request.body)
    course = get_object_or_404(Course, pk=id)

    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
    checkout_session = stripe.checkout.Session.create(
        # Customer Email is optional,
        # It is not safe to accept email directly from the client side
        # customer_email = request_data['email'],
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                     'name': course.title,
                    },
                    'unit_amount': int(course.course_price * 100),
                },
                'quantity': 1,

            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('failed')),
    )

    # OrderDetail.objects.create(
    #     customer_email=email,
    #     product=product, ......
    # )

    sub = CourseSubscription()
    # # order.customer_email = request_data['email']
    # # order.product = product
    sub.course = course
    # sub.payment_intent = checkout_session.payment_intent_data
    sub.student=StudentInfo.objects.filter(user=request.user).first()
    sub.order_id="pending"
    sub.payment_intent="payment"
    sub.payment_id="pending"
    # # order.amount = int(product.price * 100)
    sub.save()

    # return JsonResponse({'data': checkout_session})
    return JsonResponse({'sessionId': checkout_session.id})


def PaymentSuccessView(request, *args, **kwargs):

    # def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound()

        stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
        session = stripe.checkout.Session.retrieve(session_id)
        # course_title = session.line_items.price_data.name
        # course=get_object_or_404(Course,title=course_title)
        student=StudentInfo.objects.get(user=request.user)
        sub=CourseSubscription.objects.get(student=student, payment_id="pending", order_id="pending")
        # sub.student=student
        # sub = get_object_or_404(CourseSubscription, order_id="pending")
        # order.has_paid = True
        sub.payment_id="paid"
        sub.order_id="paid"
        sub.save()
        return render(request,"payment/payment_done.html")


def PaymentFailedView(request):
    render(request,"payments/payment_cancelled.html")

