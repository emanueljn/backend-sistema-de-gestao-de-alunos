from rest_framework import viewsets
from dj_rql.drf import RQLFilterBackend
from .filters import AlunoFilterClass, ProfessorFilterClass, AdministradorFilterClass
from .models import Aluno, Professor, Administrador, Historico
from .serializers import AlunoSerializer, ProfessorSerializer, AdministradorSerializer, HistoricoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = AlunoFilterClass

class HistoricoViewSet(viewsets.ModelViewSet):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = ProfessorFilterClass

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    rql_filter_class = AdministradorFilterClass
