from rest_framework import serializers
from .models import Carrera, Materia, Prerrequisito

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'

class PrerrequisitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prerrequisito
        fields = '__all__'