from rest_framework.serializers import ModelSerializer
from .models import Employer

class EmployerSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


        