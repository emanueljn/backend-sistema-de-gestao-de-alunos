from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Aluno, Professor, Administrador
class AlunoFilterClass(AutoRQLFilterClass):
    MODEL = Aluno
    FILTERS = (
        {
            'filter': 'full_name',
            'search': True,
        },
    )
class ProfessorFilterClass(AutoRQLFilterClass):
    MODEL = Professor

class AdministradorFilterClass(AutoRQLFilterClass):
    MODEL = Administrador