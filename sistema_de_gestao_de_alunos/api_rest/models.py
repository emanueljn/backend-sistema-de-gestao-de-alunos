from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=8)
    cidade = models.CharField(max_length=64)
    complemento = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.logradouro}, {self.numero}, {self.bairro}, {self.cidade}, {self.complemento}'

class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    escola = models.CharField(max_length=25)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    telefone_1  = models.CharField(max_length=11)
    telefone_2  = models.CharField(max_length=11)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )

class Administrador(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Professor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    disciplina = models.CharField(max_length=25)

class Aluno(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20, unique=True)

class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=15)
    date = models.DateField()
    def __str__(self):
        return f'Frequência de {self.aluno.user.username} em {self.date}'

class Historico(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=15)
    nota = models.FloatField(max_length=4)
    disciplina = models.CharField(max_length=25)
    escola = models.CharField(max_length=25)