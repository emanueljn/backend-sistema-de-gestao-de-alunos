from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Aluno, Professor, Administrador

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

class ProfessorFilterClass(AutoRQLFilterClass):
    MODEL = Professor

    FILTERS = (
        {
            'filter': 'full_name',
            'search': True,
        },
        {
            'filter': 'disciplina',
            'choices': Professor.DisciplinaChoices.choices,  # adicionar as opções
        }
    )

class AdministradorFilterClass(AutoRQLFilterClass):
    MODEL = Administrador