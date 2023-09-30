from django.db import models
from django.urls import reverse


class Employee(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=255)
    start_date = models.DateField(auto_now_add=True)
    salary = models.IntegerField()
    level = models.IntegerField(null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        verbose_name='Фото'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employee', kwargs={'pk': self.pk})