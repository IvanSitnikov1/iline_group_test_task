from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', employee_tree),
    path('employee-list', EmployeeList.as_view()),
]
