from django.contrib import admin
from .models import Aluno, Frequencia, Historico, CustomUser, Administrador, Professor

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class HistoricoInline(admin.TabularInline):
    model = Historico
    extra = 1

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('user', 'matricula')
    inlines = [FrequenciaInline, HistoricoInline]
    search_fields = ('user__username', 'matricula')

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'periodo', 'date')
    search_fields = ('aluno__user__username', 'periodo')

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'periodo', 'nota', 'disciplina', 'escola')
    search_fields = ('aluno__user__username', 'periodo', 'disciplina')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'cpf', 'escola', 'endereco', 'telefone_1', 'telefone_2')
    search_fields = ('full_name', 'cpf')

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('user', 'disciplina')
    search_fields = ('user__username', 'disciplina')