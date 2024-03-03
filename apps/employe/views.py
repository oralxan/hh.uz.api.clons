from rest_framework.viewsets import ModelViewSet

from .models import (
    EmployeSkill,
    Employee
)
from .serializers import (
    EmployeeSerializer,
    EmployeSkillSerializer
)
class EmployeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeSkillViewSet(ModelViewSet):
    queryset = EmployeSkill.objects.all()
    serializer_class = EmployeSkillSerializer