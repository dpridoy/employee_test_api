from django.db import models

status_info = (
    (1, 'Saved'),
    (2, 'Submitted'),
    (3, 'Approved'),
)


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return "%s" % self.name


class Company(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return "%s" % self.name


class Employee(models.Model):
    empCode = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=25, blank=True)
    address = models.CharField(max_length=100, blank=True)
    status = models.IntegerField(choices=status_info, default=0)
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return "%s" % self.name
