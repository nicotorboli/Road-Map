from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarreraViewSet, MateriaViewSet, PrerrequisitoViewSet

router = DefaultRouter()
router.register(r'carreras', CarreraViewSet)
router.register(r'materias', MateriaViewSet)
router.register(r'prerrequisitos', PrerrequisitoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]