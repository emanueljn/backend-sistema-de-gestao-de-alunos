from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

class Endereco(models.Model):
    usuario = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='enderecos', null=True)  # Usar string para evitar dependência circular
    logradouro = models.CharField(max_length=255, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.CharField(max_length=64, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
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
    email = models.EmailField(unique=True, null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True)
    escola = models.CharField(max_length=25)
    data_inscricao = models.DateTimeField(auto_now_add=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    telefone_1 = models.CharField(max_length=11, null=True, blank=True)
    telefone_2 = models.CharField(max_length=11, null=True, blank=True)

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
    class DisciplinaChoices(models.TextChoices):
        MATEMATICA = 'MT', 'Matemática'
        PORTUGUES = 'PT', 'Português'
        HISTORIA = 'HI', 'História'
        GEOGRAFIA = 'GE', 'Geografia'
        FISICA = 'FI', 'Física'
        QUIMICA = 'QU', 'Química'
        BIOLOGIA = 'BI', 'Biologia'

    disciplina = models.CharField(
        max_length=2,
        choices=DisciplinaChoices.choices
    )

class Aluno(CustomUser):
    matricula = models.CharField(max_length=20, unique=True)
    cadastrado_no_ensino_medido = models.BooleanField(default=False)

class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=15)
    date = models.DateField()
    def __str__(self):
        return f'Frequência de {self.aluno.user.full_name} em {self.date}'

class Historico(models.Model):
    class DisciplinaChoices(models.TextChoices):
        MATEMATICA = 'MT', 'Matemática'
        PORTUGUES = 'PT', 'Português'
        HISTORIA = 'HI', 'História'
        GEOGRAFIA = 'GE', 'Geografia'
        FISICA = 'FI', 'Física'
        QUIMICA = 'QU', 'Química'
        BIOLOGIA = 'BI', 'Biologia'

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    escola = models.CharField(max_length=25)
    periodo = models.CharField(max_length=15)
    disciplina = models.CharField(
        max_length=2,
        choices=DisciplinaChoices.choices
    )
    nota1 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    nota2 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    nota3 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    nota4 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    nota_final = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.disciplina} - Nota Final: {self.nota_final}'