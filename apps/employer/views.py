from rest_framework.viewsets import ModelViewSet

from .models import Employer
from.serializers import EmployerSerializer
class EmployerViewSet(ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    