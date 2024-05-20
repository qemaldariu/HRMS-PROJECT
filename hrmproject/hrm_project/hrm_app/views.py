from django.core.paginator import Paginator
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.views import FilterView
from rest_framework import filters  # Import filters from rest_framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import EmployeeSerializer, DepartmentSerializer
from .models import Employee, Department
from .filters import EmployeeFilter

class Department(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class EmployeeListCreate(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department']
    ordering_fields = ['salary']

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        queryset = super().get_queryset()
        department = self.request.query_params.get('department')
        if department:
            queryset = queryset.filter(department_id=department)
        return queryset.order_by('-salary')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)  # Paginate queryset
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class EmployeeCreate(CreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class EmployeeModifyRetrieveDelete(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()

    def perform_update(self, serializer):
        serializer.save()

