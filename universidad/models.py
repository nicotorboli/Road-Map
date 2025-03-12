from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    horas_semanales = models.IntegerField()
    carga_horaria_total = models.IntegerField()
    creditos = models.IntegerField()
    regimen_cursado = models.CharField(max_length=20)
    cuatrimestre = models.CharField(max_length=10)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Prerrequisito(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='materia_principal')
    prerrequisito = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='materia_prerrequisito')

    def __str__(self):
        return f"{self.materia.nombre} requiere {self.prerrequisito.nombre}"
