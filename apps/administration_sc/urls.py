from django.urls import path

from .views import *

urlpatterns=[
        path('list_students/',student_list.as_view(),name="students-people"),
        path('list_courses/',course_list.as_view(),name="courses-people"),
        path('list_teachers/',teacher_list.as_view(),name="teachers-people"),
        #Update Urls Actions
        path('update_student/<int:pk>/', update_student.as_view(), name='update_student'),
        path('update_teacher/<int:pk>/', update_teacher.as_view(), name='update_teacher'),
        path('update_course/<int:pk>/', update_course.as_view(), name='update_course'),
        #Delete Urls Actions
        path('delete_student/<int:pk>/', delete_student.as_view()),
        path('delete_teacher/<int:pk>/', delete_teacher.as_view()),
        path('delete_course/<int:pk>/', delete_course.as_view()),
]