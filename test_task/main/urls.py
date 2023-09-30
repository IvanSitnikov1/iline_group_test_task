from django.urls import path

from .views import *
from test_task.views import index

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>', employee_tree, name='tree'),
    path('employee-list', EmployeeList.as_view(), name='list'),
    path('employee/create', CreateEmployee.as_view(), name='create'),
    path('employee/<int:pk>', ShowEmployee.as_view(), name='read'),
    path('employee/update/<int:pk>', UpdateEmployee.as_view(), name='update'),
    path('employee/delete/<int:pk>', delete, name='delete'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]
