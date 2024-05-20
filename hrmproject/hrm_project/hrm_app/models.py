import datetime

from django.db import models
from django.utils import timezone

EMPLOYEE_GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department

class Employee(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=100,default=None)

    address = models.CharField(max_length=255, default=None)
    birthplace = models.CharField(max_length=50 ,default=None)
    birthday = models.DateField(default=None)
    datejoined = models.DateField(default=datetime.date.today()
                                  )

    salary = models.FloatField(default=0)





    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
