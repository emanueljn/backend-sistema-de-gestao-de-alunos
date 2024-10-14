from rest_framework import viewsets
from dj_rql.drf import RQLFilterBackend
from .filters import AlunoFilterClass, ProfessorFilterClass, AdministradorFilterClass, HistoricoFilterClass
from .models import Aluno, Professor, Administrador, Historico
from .serializers import AlunoSerializer, ProfessorSerializer, AdministradorSerializer, HistoricoSerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

class AlunoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = AlunoFilterClass

class HistoricoViewSet(viewsets.ModelViewSet):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = HistoricoFilterClass

    def get_queryset(self):
        queryset = super().get_queryset()
        aluno_id = self.request.query_params.get('aluno_id', None)

        # Filtra por aluno_id, se presente
        if aluno_id is not None:
            queryset = queryset.filter(Q(aluno_id=aluno_id))

        return queryset

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = ProfessorFilterClass

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    rql_filter_class = AdministradorFilterClass
