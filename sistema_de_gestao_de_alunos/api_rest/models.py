from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _

class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=8)
    cidade = models.CharField(max_length=64)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    complemento = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.logradouro}, {self.numero}, {self.bairro}, {self.cidade}, {self.complemento}'


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, cpf, email, password, **extra_fields):
        """
        Cria e salva um usuário com o cpf, e-mail e senha fornecidos.
        """
        if not cpf:
            raise ValueError(_("The given CPF must be set"))
        email = self.normalize_email(email)
        user = self.model(cpf=cpf, email=email, **extra_fields)
        user.set_password(password)  # Use set_password para criptografar a senha
        user.save(using=self._db)
        return user

    def create_user(self, cpf, email=None, password=None, **extra_fields):
        """
        Cria um usuário normal.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(cpf, email, password, **extra_fields)

    def create_superuser(self, cpf, email=None, password=None, **extra_fields):
        """
        Cria um superusuário.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self._create_user(cpf, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    cpf = models.CharField(max_length=11, unique=True)
    escola = models.CharField(max_length=25)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    telefone_1 = models.CharField(max_length=11)
    telefone_2 = models.CharField(max_length=11)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['full_name', 'escola']  # Campos obrigatórios para criar um superusuário

    is_active = models.BooleanField(default=True)  # Valor padrão adicionado
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.cpf

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