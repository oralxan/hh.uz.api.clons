from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Vacancy
from .serializers import VacancySerializer
class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [AllowAny()]