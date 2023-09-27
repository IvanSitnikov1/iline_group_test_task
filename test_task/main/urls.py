from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', employee_tree),
    path('employee-list', EmployeeList.as_view()),
    path('employee/create', CreateEmployee.as_view()),
    path('employee/read/<int:id>', ShowEmployee.as_view()),
    path('employee/update/<int:id>', UpdateEmployee.as_view()),
    path('employee/delete/<int:id>', DeleteEmployee.as_view()),
]
