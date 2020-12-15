from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.list_students, name='students'),
    path('student/add', views.add_student, name='add_student'),
    path('student/edit/<int:student_id>', views.edit_student, name='edit_student'),
    path('student/delete/<int:student_id>', views.delete_student, name='delete_student'),
    path('teachers/', views.list_teachers, name='teachers'),
    path('teacher/add', views.add_teacher, name='add_teacher'),
    path('teacher/edit/<int:teacher_id>', views.edit_teacher, name='edit_teacher'),
    path('teacher/delete/<int:teacher_id>', views.delete_teacher, name='delete_teacher'),
]
