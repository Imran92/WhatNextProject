from rest_framework import serializers
from .models import  *

class AdmissionRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionRequirement
        fields = '__all__'


class DegreeAdmissionRequirementSerializer(serializers.ModelSerializer):
    admissionrequirement = AdmissionRequirementSerializer(required=True)
    class Meta:
        model = DegreeRequirement
        fields = '__all__'

class DegreeSerializer(serializers.ModelSerializer):
    admissionrequirements = DegreeAdmissionRequirementSerializer(required=False, many=True)
    class Meta:
        model = Degree
        fields = ['id','varsity','department','varsity_id','department_id','admissionrequirements','name',
                  'years','cost','semesters','credits','degreelevel']

class DepartmentSerializer(serializers.ModelSerializer):
    degrees = DegreeSerializer(required=False, many=True)
    class Meta:
        model = Department
        fields = ['id','name','varsity','varsity_id','departmenttype','degrees']


class VarsitySerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(required=False, many=True)
    degrees = DegreeSerializer(required=False, many=True)
    class Meta:
        model = Varsity
        address = serializers.CharField(max_length=200, required=False, allow_blank=True)
        fields = ['id','name','varsitycategory','address','phone','email','website','fax','district','established','category','newsandevent','admissioninfo','departments','degrees']
        read_only_fields = ['departments']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


