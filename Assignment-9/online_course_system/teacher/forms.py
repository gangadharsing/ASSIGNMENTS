from django import forms
from course.models import Course
#DataFlair
class CourseCreate(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'