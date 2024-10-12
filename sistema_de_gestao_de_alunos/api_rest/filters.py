from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Aluno, Professor, Administrador, Historico

class AlunoFilterClass(AutoRQLFilterClass):
    MODEL = Aluno

    FILTERS = (
        {
            'filter': 'full_name',
            'search': True,
        },
        {
            'filter': 'data_inscricao',
            'field_type': 'datetime',  # Defina o tipo de campo como datetime
        }
    )

class HistoricoFilterClass(AutoRQLFilterClass):
    MODEL = Historico

    FILTERS = (
        'id',
        'aluno.id',  # Acessa o campo `id` do modelo Aluno, via a ForeignKey 'aluno'
    )

class ProfessorFilterClass(AutoRQLFilterClass):
    MODEL = Professor

    FILTERS = (
        'id',  # Filtrar por ID de Historico se necessário
        'aluno_id',  # Filtrar pelo campo aluno_id que é o ID da ForeignKey
    )

class AdministradorFilterClass(AutoRQLFilterClass):
    MODEL = Administrador