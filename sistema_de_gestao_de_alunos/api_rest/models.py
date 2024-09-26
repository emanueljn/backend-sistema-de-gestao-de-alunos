from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

class Endereco(models.Model):
    usuario = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='enderecos', null=True)  # Usar string para evitar dependência circular
    logradouro = models.CharField(max_length=255, null=True)
    numero = models.IntegerField(null=True)
    bairro = models.CharField(max_length=30, null=True)
    cidade = models.CharField(max_length=64, null=True)
    uf = models.CharField(max_length=2, null=True)
    cep = models.CharField(max_length=8, null=True)
    complemento = models.CharField(max_length=100, null=True)
    def __str__(self):
        return f'{self.logradouro}, {self.numero}, {self.bairro}, {self.cidade}, {self.complemento}'

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, cpf, email, password, **extra_fields):
        if not cpf:
            raise ValueError(_("The given CPF must be set"))
        email = self.normalize_email(email)
        user = self.model(cpf=cpf, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, cpf, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(cpf, email, password, **extra_fields)

    def create_superuser(self, cpf, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self._create_user(cpf, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    escola = models.CharField(max_length=25)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    telefone_1 = models.CharField(max_length=11, null=True)
    telefone_2 = models.CharField(max_length=11, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'cpf']

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.cpf

class Administrador(CustomUser):
    departamento = models.CharField(max_length=50)

class Professor(CustomUser):
    disciplina = models.CharField(max_length=25)

class Aluno(CustomUser):
    matricula = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True, null=True)

class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=15)
    date = models.DateField()
    def __str__(self):
        return f'Frequência de {self.aluno.user.full_name} em {self.date}'

class Historico(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=15)
    nota = models.FloatField(max_length=4)
    disciplina = models.CharField(max_length=25)
    escola = models.CharField(max_length=25)