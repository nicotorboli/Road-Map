from rest_framework import viewsets
from .models import Carrera, Materia, Prerrequisito
from .serializers import CarreraSerializer, MateriaSerializer, PrerrequisitoSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class PrerrequisitoViewSet(viewsets.ModelViewSet):
    queryset = Prerrequisito.objects.all()
    serializer_class = PrerrequisitoSerializer

# Create your views here.
