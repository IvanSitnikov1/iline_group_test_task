from django.shortcuts import render
from django.views.generic import ListView

from .models import *


def employee(request):
    employees = Employee.objects.all()
    cats = {}
    for i in employees:
        if i.parent_id in cats:
            cats[i.parent_id].append(i)
        else:
            cats[i.parent_id] = [i]
    tree = build_tree(cats, 1, 3)
    boss = Employee.objects.get(parent_id__isnull=True)
    context = {'boss': boss, 'tree': tree}
    return render(request, 'main/base.html', context)


def build_tree(cats, parent_id, lvl):
    lvl -= 1
    if parent_id in cats:
        tree = '<ul>'
        for i in cats[parent_id]:
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
