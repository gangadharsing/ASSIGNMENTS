from django.shortcuts import get_object_or_404
from .models import Course
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from student.models import CourseSubscription, StudentInfo
from django.shortcuts import redirect


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
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