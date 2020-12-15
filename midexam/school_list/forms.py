from django.forms import ModelForm
from django.core.exceptions import ValidationError
from school_list.models import Student,Teacher

class StudentForm(ModelForm):
    class Meta:
        model= Student
        fields= ['s_name', 's_class', 's_dob', 's_address', 's_phonenum', 's_email']

class TeacherForm(ModelForm):
    class Meta:
        model= Teacher
        fields= ['t_name', 't_subject', 't_dob', 't_address', 't_phonenum', 't_email']