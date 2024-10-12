from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, ProfessorViewSet, AdministradorViewSet, HistoricoViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'historico', HistoricoViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'administradores', AdministradorViewSet)

# URLs
urlpatterns = [
    path('', include(router.urls)),
]
