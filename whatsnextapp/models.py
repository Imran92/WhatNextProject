from django.db import models
from django_enumfield import enum
from .enums import *

# Create your models here.
class Varsity(models.Model):
    name = models.CharField(max_length=200)
    varsitycategory = enum.EnumField(VarsityCategory, default=VarsityCategory.PUBLIC)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    fax = models.CharField(max_length=100)
    district = models.CharField(max_length=200)
    established = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    newsandevent = models.TextField(max_length=200)
    admissioninfo = models.TextField(max_length=500)

class Department(models.Model):
    name = models.CharField(max_length=200)
    varsity = models.ForeignKey(Varsity, related_name='departments', on_delete=models.CASCADE)
    departmenttype = enum.EnumField(DepartmentCategory, default=DepartmentCategory.SCIENCE)

class Degree(models.Model):
    varsity = models.ForeignKey(Varsity, related_name='degrees', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='degrees', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    years = models.IntegerField()
    cost = models.IntegerField()
    semesters = models.IntegerField()
    credits = models.IntegerField()
    degreelevel = enum.EnumField(DegreeLevel, default=DegreeLevel.BACHELORS)

class AdmissionRequirement(models.Model):
    requirementtype = enum.EnumField(RequirementType, default=RequirementType.GRADE)
    Value = models.CharField(max_length=200)
    level = enum.EnumField(RequirementLevel, default=RequirementLevel.HSC)

class DegreeRequirement(models.Model):
    admissionrequirement = models.ForeignKey(AdmissionRequirement, related_name='requirementdegrees', on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, related_name='admissionrequirements', on_delete=models.CASCADE)

class Subject(models.Model):
    name = models.CharField(max_length=200)
    level = enum.EnumField(SchoolLevel, default=SchoolLevel.HSC)
    discipline = enum.EnumField(Discipline, default=Discipline.SCIENCE)

class RequirementSubject(models.Model):
    admissionrequirement = models.ForeignKey(AdmissionRequirement, related_name='requirementsubjects', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='subjectrequirements', on_delete=models.CASCADE)