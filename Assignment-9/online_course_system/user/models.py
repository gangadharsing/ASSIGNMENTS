from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

USER_TYPE = [
    ("STUDENT", "STUDENT"),
    ("TEACHER", "TEACHER"),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=8, choices=USER_TYPE, default="STUDENT")
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=12)
    # dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.user.email} - {self.mobile_no}"


class OTPLog(models.Model):
    email = models.EmailField(blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.otp)
