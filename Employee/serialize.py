from rest_framework import serializers
from Employee.models import Employeee, Department

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employeee
        fields=('id','url','name','department')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Department
        fields=('id','url','name')