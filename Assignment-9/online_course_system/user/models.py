from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _



class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(_('email address'), unique=True)
    mobile_no = models.CharField(max_length=12)
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.username.email} - {self.mobile_no}"



class OTPLog(models.Model):
    email = models.EmailField(blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.otp)
