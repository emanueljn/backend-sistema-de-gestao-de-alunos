from django.contrib import admin
from .models import Aluno, Frequencia, Historico, Administrador, Professor, Endereco

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class HistoricoInline(admin.TabularInline):
    model = Historico
    extra = 1

class EnderecoInline(admin.TabularInline):
    model = Endereco
    extra = 1  # Número de formulários extras a serem exibidos

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'matricula', 'email', 'cpf', 'escola', 'telefone_1', 'telefone_2', 'cadastrado_no_ensino_medido')
    inlines = [FrequenciaInline, HistoricoInline, EnderecoInline]
    search_fields = ('full_name', 'matricula')
    exclude = ('password',"endereco",)

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'date')
    search_fields = ('periodo', 'date')

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'nota1','nota2','nota3','nota4','nota_final', 'disciplina', 'escola')
    search_fields = ('periodo', 'disciplina')

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'cpf', 'escola', 'telefone_1', 'telefone_2')
    search_fields = ('full_name',)
    inlines = [EnderecoInline]
    exclude = ("endereco",)

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'cpf', 'escola', 'telefone_1', 'telefone_2')
    search_fields = ('full_name', 'disciplina')
    inlines = [EnderecoInline]
    exclude = ("endereco",)