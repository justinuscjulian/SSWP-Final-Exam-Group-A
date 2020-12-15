from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from school_list.models import Student,Teacher
from school_list.forms import StudentForm,TeacherForm

# Create your views here.
def index(request):
    num_students= Student.objects.all().count()
    num_teachers= Teacher.objects.all().count()
    context={
        'num_students':num_students,
        'num_teachers':num_teachers,
    }
    return render(request, 'index.html', context=context)

def list_students(request):
    students= Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'students.html', context=context)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentForm()

    context = {
        'form': form
    }
    return render(request, 'student_form.html', context=context)

def edit_student(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(pk=student_id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        student = Student.objects.get(pk=student_id)
        fields = model_to_dict(student)
        form = StudentForm(initial=fields, instance=student)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'student_form.html', context=context)


def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students'))
    context = {
        'student': student
    }
    return render(request, 'student_delete_form.html', context=context)

def list_teachers(request):
    teachers= Teacher.objects.all()
    context = {
        'teachers': teachers,
    }
    return render(request, 'teachers.html', context=context)

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherForm()

    context = {
        'form': form
    }
    return render(request, 'teachers_form.html', context=context)

def edit_teacher(request, teacher_id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk=teacher_id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        teacher = Teacher.objects.get(pk=teacher_id)
        fields = model_to_dict(teacher)
        form = TeacherForm(initial=fields, instance=teacher)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'teachers_form.html', context=context)


def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers'))
    context = {
        'teacher': teacher
    }
    return render(request, 'teachers_delete_form.html', context=context)