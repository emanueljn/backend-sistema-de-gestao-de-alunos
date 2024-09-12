from rest_framework import serializers
from .models import Aluno, Professor, Administrador, Frequencia, Historico, CustomUser, Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()

    class Meta:
        model = CustomUser
        fields = ['username', 'cpf', 'escola', 'endereco', 'telefone_1', 'telefone_2']

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        endereco, created = Endereco.objects.get_or_create(**endereco_data)
        user = CustomUser.objects.create(**validated_data, endereco=endereco)
        return user

    def update(self, instance, validated_data):
        endereco_data = validated_data.pop('endereco', None)
        if endereco_data:
            if instance.endereco:
                for attr, value in endereco_data.items():
                    setattr(instance.endereco, attr, value)
                instance.endereco.save()
            else:
                endereco, created = Endereco.objects.get_or_create(**endereco_data)
                instance.endereco = endereco
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
    user = CustomUserSerializer()
    frequencias = FrequenciaSerializer(many=True, required=False, read_only=True)
    historicos = HistoricoSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Aluno
        fields = ['user', 'matricula', 'frequencias', 'historicos']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = CustomUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        aluno = Aluno.objects.create(user=user, **validated_data)
        return aluno

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = CustomUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        professor = Professor.objects.create(user=user, **validated_data)
        return professor

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'
