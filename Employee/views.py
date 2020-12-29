from django.shortcuts import render
from rest_framework import viewsets,permissions
from Employee.models import Employeee,Department
from .serialize import EmployeeSerializer,DepartmentSerializer
import requests
from django.shortcuts import render

# Create your views here.

class EmployeeView(viewsets.ModelViewSet):
    queryset=Employeee.objects.all()
    serializer_class=EmployeeSerializer

class DepartmentView(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    
    
    #permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    