from django.urls import path
from .views import EmployeeListCreate, EmployeeModifyRetrieveDelete, EmployeeCreate,EmployeeFilter,Department

urlpatterns = [
    path("create_employee_list/", EmployeeListCreate.as_view(), name='create_employee_list'),
    path("create_department_list/", Department.as_view(), name='create_department_list'),

    path("new_employee/", EmployeeCreate.as_view(), name='create_employee'),

    path("modify_employee/<int:pk>/", EmployeeModifyRetrieveDelete.as_view(), name='modify_employee'),
    path("delete_employee/<int:pk>/", EmployeeModifyRetrieveDelete.as_view(), name='delete_employee'),
    # path("employees/filter/", EmployeeFilter.as_view(), name='employee-filter-by-department'),

]

