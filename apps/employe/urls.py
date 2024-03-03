from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    EmployeViewSet,
    EmployeSkillViewSet
)

router = DefaultRouter()
router.register('emplyer', EmployeViewSet, basename='employee')
router.register('EmployeSkillViewSet',EmployeSkillViewSet, basename='EmployeSkillViewSet')

urlpatterns = []
urlpatterns += router.urls
