from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=255)
    start_date = models.DateField(auto_now_add=True)
    salary = models.IntegerField()
    level = models.IntegerField(null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']