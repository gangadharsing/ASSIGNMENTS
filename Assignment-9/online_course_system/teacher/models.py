from django.db import models
from django.contrib.auth.models import User
from course.models import Course
from django.utils.timezone import now
# Create your models here.
class TeacherInfo(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email_id = models.EmailField(default="-")
    mobile_no = models.CharField(max_length=12)
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.username.email} - {self.mobile_no}"

class CourseAdded(models.Model):
    teacher = models.ForeignKey(TeacherInfo, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher.username} ==== {self.course}"