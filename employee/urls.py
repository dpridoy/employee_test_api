from django.urls import path
from .views import CompanyApiVIEW, DepartmentApiVIEW, EmployeeApiVIEW, EmployeeDeleteApiView, EmployeeSubmitApiView, \
    EmployeeUnAssignedApiVIEW, EmployeeUnSubmittedApiVIEW

urlpatterns = [
    path('company/list/', CompanyApiVIEW.as_view()),
    path('department/list/', DepartmentApiVIEW.as_view()),
    path('employee/list/', EmployeeApiVIEW.as_view()),
    path('employee/saved/list/', EmployeeUnAssignedApiVIEW.as_view()),
    path('employee/submitted/list/', EmployeeUnSubmittedApiVIEW.as_view()),
    path('employee/delete/', EmployeeDeleteApiView.as_view()),
    path('employee/status/update/', EmployeeSubmitApiView.as_view()),

]
