from django.urls import path

from .views import *

urlpatterns=[
        path('list_people/',people_list.as_view(),name="list-people"),
]