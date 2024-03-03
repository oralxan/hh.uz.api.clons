from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EmployerViewSet

router = DefaultRouter()
router.register('emplyer', EmployerViewSet, basename='employer')

urlpatterns = []
urlpatterns += router.urls
