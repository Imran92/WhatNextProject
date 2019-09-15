from django.shortcuts import render
from django.http import request
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
def hudai(request):
    vars = Varsity(name="Fal Vars", varsitycategory= 2)
    vars.save()
    return JsonResponse({'data':'dhur chata'})

class VarsityCrud(viewsets.ModelViewSet):
    queryset = Varsity.objects.all()
    serializer_class = VarsitySerializer
    def get_list(request, format=None):
        usrs = [varsity.name for varsity in Varsity.objects.all()]
        return  Response(usrs)

class DepartmentCrud(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    def get_list(request, format=None):
        usrs = [department.name for department in Department.objects.all()]
        return  Response(usrs)

class DegreeCrud(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    def get_object(self):
        return JsonResponse({"dhur": "ghora"})
    def __get__(self, instance, owner):
        return JsonResponse({"dhur": "ghora"})

class AdmissionRequirementCrud(viewsets.ModelViewSet):
    queryset = AdmissionRequirement.objects.all()
    serializer_class = AdmissionRequirementSerializer

class SubjectCrud(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class DegreeAdmissionRequirementCrud(viewsets.ModelViewSet):
    queryset = DegreeRequirement.objects.all()
    serializer_class = DegreeAdmissionRequirementSerializer
