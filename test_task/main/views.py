from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .forms import *
from .models import *


class CreateEmployee(LoginRequiredMixin, CreateView):
    login_url = "/login/"
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


class UpdateEmployee(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Employee
    form_class = CreateEmployeeForm
    template_name = 'main/update_employee.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('read', kwargs={'pk': pk})


@login_required(login_url="/login/")
def delete(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('list')


class EmployeeList(ListView):
    paginate_by = 10
    model = Employee
    template_name = 'main/employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            queryset = Employee.objects.filter(
                Q(name=query) | Q(position=query) | Q(parent__name=query)
            )
        else:
            queryset = Employee.objects.all().order_by('-pk')
        return queryset


def employee_tree(request, pk):
    def build_tree(parent, lvl):
        lvl -= 1
        tree = '<ul>'
        for i in Employee.objects.filter(parent=parent):
            if lvl != 0:
                tree += f'<li><a style="color: #003d7b;" href="/{i.pk}">{i.name} - Должность: {i.position}</a></li>'
                tree += build_tree(i, lvl)
        tree += '</ul>'
        return tree
    boss = Employee.objects.get(pk=pk)
    tree = build_tree(boss, 2)
    context = {'boss': boss, 'tree': tree}
    return render(request, 'main/employee_tree.html', context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'


def logout_user(request):
    logout(request)
    return redirect('login')