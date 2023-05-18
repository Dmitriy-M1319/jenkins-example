from rest_framework import viewsets

from api.models import CarModel
from .serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
