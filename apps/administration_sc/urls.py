from django.urls import path

from .views import *

urlpatterns=[
        path('list_students/',student_list.as_view(),name="students-people"),
        path('list_courses/',course_list.as_view(),name="courses-people"),
        path('list_teachers/',teacher_list.as_view(),name="teachers-people"),
]