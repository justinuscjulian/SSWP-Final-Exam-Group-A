from django.db import models

# Create your models here.
class Student(models.Model):
    s_name= models.CharField('Name',max_length=30)
    s_class= models.CharField('Class',max_length=10)
    s_dob= models.DateField('Date of Birth',null=True)
    s_address= models.CharField('Address',max_length=50)
    s_phonenum= models.CharField('Phone Number:',max_length=20)
    s_email= models.CharField('E-mail',max_length=30)
    
    def __str__(self):
        return f'{self.s_name}, {self.s_class}'

class Teacher(models.Model):
    t_name= models.CharField('Name',max_length=30)
    t_subject= models.CharField('Subject',max_length=30)
    t_dob= models.DateField('Date of Birth',null=True)
    t_address= models.CharField('Address',max_length=50)
    t_phonenum= models.CharField('Phone Number:',max_length=20)
    t_email= models.CharField('E-mail',max_length=30)

    def __str__(self):
        return f'{self.t_name}, {self.t_subject}'