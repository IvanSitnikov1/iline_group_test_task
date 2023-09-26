from django.shortcuts import render
from django.views.generic import ListView

from .models import *


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
                tree += build_tree(cats, i.id, lvl)
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
    tree = build_tree(employee_dict, 1, 3)
    boss = Employee.objects.get(parent_id__isnull=True)
    context = {'boss': boss, 'tree': tree}
    return render(request, 'main/employee_tree.html', context)





