from rest_framework import serializers
from .models import Company, Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['id', 'name']


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id', 'name']
        depth = 1


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['empCode', 'name', 'phone', 'status', 'department', 'company', 'address']
        depth = 1