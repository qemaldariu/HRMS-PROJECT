from django.contrib import admin
from .models import Employee, Department

# Register the Employee model with the admin site
admin.site.register(Employee)
admin.site.register(Department)
