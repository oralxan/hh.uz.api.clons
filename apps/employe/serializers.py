from rest_framework.serializers import ModelSerializer
from .models import (
    Employee,
    EmployeSkill
)

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeSkillSerializer(ModelSerializer):
    class Meta:
        model = EmployeSkill
        fields = '__all__'
        

        