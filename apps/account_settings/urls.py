from django.urls import path

from .views import *

app_name = 'apps.account_settings'

urlpatterns = [
    #update accounts
    path('update_student/<int:pk>/', update_student.as_view(), name='update_student'),
    path('update_teacher/<int:pk>/', update_teacher.as_view(), name='update_teacher'),
]
