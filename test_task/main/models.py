from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Employee(MPTTModel):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=255)
    start_date = models.DateField(auto_now_add=True)
    salary = models.IntegerField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']