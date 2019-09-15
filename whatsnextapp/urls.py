from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('varsities', views.VarsityCrud)
router.register('departments', views.DepartmentCrud)
router.register('degrees', views.DegreeCrud)
router.register('admission-requirements', views.AdmissionRequirementCrud)
router.register('degree-admission-requirements', views.DegreeAdmissionRequirementCrud)
router.register('subjects', views.SubjectCrud)

urlpatterns = [
    path('', include(router.urls))
]