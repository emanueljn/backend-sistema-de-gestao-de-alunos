from rest_framework import serializers
from .models import Aluno, Professor, Administrador, Frequencia, Historico, CustomUser, Endereco

from rest_framework import serializers
from .models import Aluno, Professor, Administrador, Frequencia, Historico, CustomUser, Endereco

from rest_framework import serializers
from .models import Aluno, Professor, Administrador, Frequencia, Historico, CustomUser, Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'logradouro', 'numero', 'bairro', 'cidade', 'uf', 'cep', 'complemento']

class CustomUserSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'full_name', 'email', 'cpf', 'escola', 'telefone_1', 'telefone_2', 'endereco']

    def create(self, validated_data):
        # Extrai os dados do endereço
        endereco_data = validated_data.pop('endereco')
        # Cria o endereço
        endereco = Endereco.objects.create(**endereco_data)
        # Cria o usuário
        user = CustomUser.objects.create(**validated_data, endereco=endereco)
        return user

    def update(self, instance, validated_data):
        endereco_data = validated_data.pop('endereco', None)
        if endereco_data:
            for attr, value in endereco_data.items():
                setattr(instance.endereco, attr, value)
            instance.endereco.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class FrequenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequencia
        fields = '__all__'

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()

    class Meta:
        model = Aluno
        fields = ['id', 'full_name', 'matricula', 'email', 'cpf', 'escola', 'telefone_1', 'telefone_2', 'endereco']

    def create(self, validated_data):
        # Extrai os dados do endereço
        endereco_data = validated_data.pop('endereco')

        # Cria o endereço
        endereco = Endereco.objects.create(**endereco_data)

        # Cria o aluno e associa o endereço
        aluno = Aluno.objects.create(endereco=endereco, **validated_data)  # Passa os dados restantes para Aluno
        return aluno

class ProfessorSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()

    class Meta:
        model = Professor
        fields = ['id', 'full_name', 'disciplina', 'email', 'cpf', 'escola', 'telefone_1', 'telefone_2', 'endereco']

    def create(self, validated_data):
        # Extrai os dados do endereço
        endereco_data = validated_data.pop('endereco')

        # Cria o endereço
        endereco = Endereco.objects.create(**endereco_data)

        # Cria o professor e associa o endereço
        professor = Professor.objects.create(endereco=endereco, **validated_data)
        return professor

class AdministradorSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()

    class Meta:
        model = Administrador
        fields = ['id', 'full_name', 'departamento', 'email', 'cpf', 'escola', 'telefone_1', 'telefone_2', 'endereco']

    def create(self, validated_data):
        # Extrai os dados do endereço
        endereco_data = validated_data.pop('endereco')

        # Cria o endereço
        endereco = Endereco.objects.create(**endereco_data)

        # Cria o administrador e associa o endereço
        administrador = Administrador.objects.create(endereco=endereco, **validated_data)
        return administrador
