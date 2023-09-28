from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .forms import *
from .models import *


class CreateEmployee(CreateView):
    form_class = CreateEmployeeForm
    template_name = 'main/create_employee.html'

    def form_valid(self, form):
        employee = form.save(commit=False)
        employee.level = employee.parent.level + 1
        employee.save()
        return redirect('read', pk=employee.pk)



class ShowEmployee(DetailView):
    model = Employee
    template_name = 'main/show_employee.html'
    context_object_name = 'employee'


class UpdateEmployee(UpdateView):
    model = Employee
    form_class = CreateEmployeeForm
    template_name = 'main/update_employee.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('read', kwargs={'pk': pk})


def delete(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('list')


class EmployeeList(ListView):
    model = Employee
    template_name = 'main/employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return Employee.objects.all().order_by('-pk')[:10]


def employee_tree(request):
    def build_tree(employee_dict, parent_id, lvl):
        lvl -= 1
        if parent_id in employee_dict:
            tree = '<ul>'
            for i in employee_dict[parent_id]:
                if lvl == 0:
                    tree += f'<li style="display: none">{i.name} - {i.position}'
                else:
                    tree += f'<li>{i.name} - {i.position}'
                tree += build_tree(employee_dict, i.id, lvl)
                tree += '</li>'
            tree += '</ul>'
        else:
            return ''
        return tree

    employees = Employee.objects.all()
    employee_dict = {}
    for i in employees:
        if i.parent_id in employee_dict:
            employee_dict[i.parent_id].append(i)
        else:
            employee_dict[i.parent_id] = [i]
    tree = build_tree(employee_dict, 1, 4)
    boss = Employee.objects.get(parent_id__isnull=True)
    context = {'boss': boss, 'tree': tree}
    return render(request, 'main/employee_tree.html', context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('tree')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'


def logout_user(request):
    logout(request)
    return redirect('login')