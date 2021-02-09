from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company, Department, Employee
from .serializers import CompanySerializer, DepartmentSerializer, EmployeeSerializer


class CompanyApiVIEW(APIView):

    def get(self, request):
        student = Company.objects.all()
        serializer = CompanySerializer(student, many=True)
        return Response(serializer.data)


class DepartmentApiVIEW(APIView):

    def get(self, request):
        key = Department.objects.all()
        serializer = DepartmentSerializer(key, many=True)
        return Response(serializer.data)


class EmployeeApiVIEW(APIView):

    def get(self, request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self, request):
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'Employee Added Successfully',
        }
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(response, status=status.HTTP_200_OK)
        response['status code'] = status.HTTP_400_BAD_REQUEST
        response['success'] = 'False'
        response['message'] = 'Failed'
        return Response(response)


class EmployeeUnAssignedApiVIEW(APIView):

    def get(self, request):
        emp = Employee.objects.filter(status=1)
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)


class EmployeeUnSubmittedApiVIEW(APIView):

    def get(self, request):
        emp = Employee.objects.filter(status=2)
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)


class EmployeeDeleteApiView(APIView):
    def post(self, request):
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'Deleted Successfully',
        }
        e_code = request.data.get('empCode')
        emp = Employee.objects.get(empCode=e_code)
        emp.delete()
        return Response(response)


class EmployeeSubmitApiView(APIView):
    def post(self, request):
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'Employee List Submitted Successfully',
        }
        emp_list = Employee.objects.filter(status=1)
        stat = request.data.get('status')
        company = request.data.get('company')
        print(company)
        department = request.data.get('department')
        print(department)
        print(emp_list.update(status=stat, company=Company.objects.get(name=company), department=Department.objects.get(name=department)))

        return Response(response)


