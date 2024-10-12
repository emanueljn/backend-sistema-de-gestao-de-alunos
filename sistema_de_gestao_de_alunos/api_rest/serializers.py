from rest_framework import serializers
from .models import Aluno, Professor, Administrador, Frequencia, Historico, CustomUser, Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    numero = serializers.IntegerField(required=False, allow_null=True)

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
    endereco = EnderecoSerializer(required=False, allow_null=True)  # Endereco é opcional

    class Meta:
        model = Aluno
        fields = ['id', 'full_name', 'matricula', 'email', 'cpf', 'escola', 'data_inscricao', 'telefone_1',
                  'telefone_2', 'endereco']
        read_only_fields = ['data_inscricao']

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco', None)  # Remove o campo endereco se não existir

        if endereco_data:
            # Se houver dados de endereço, validamos e criamos o endereço
            endereco_serializer = EnderecoSerializer(data=endereco_data)
            endereco_serializer.is_valid(raise_exception=True)  # Valida apenas se houver dados de endereço
            endereco = endereco_serializer.save()
            aluno = Aluno.objects.create(endereco=endereco, **validated_data)
        else:
            # Se nenhum endereço for enviado, criamos o aluno sem endereço
            aluno = Aluno.objects.create(**validated_data)

        return aluno

    def validate(self, data):
        # Validação personalizada: só valida o endereço se ele for passado
        endereco_data = data.get('endereco')
        if endereco_data:
            # Validamos o serializer do endereço apenas se houver dados
            endereco_serializer = EnderecoSerializer(data=endereco_data)
            endereco_serializer.is_valid(raise_exception=True)
        return data

class ProfessorSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(required=False, allow_null=True)  # Endereco é opcional

    class Meta:
        model = Professor
        fields = ['id', 'full_name', 'disciplina', 'email', 'cpf', 'escola', 'data_inscricao', 'telefone_1',
                  'telefone_2', 'endereco']

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco', None)  # Remove o campo endereco se não existir

        if endereco_data:
            # Se houver dados de endereço, validamos e criamos o endereço
            endereco_serializer = EnderecoSerializer(data=endereco_data)
            endereco_serializer.is_valid(raise_exception=True)  # Valida apenas se houver dados de endereço
            endereco = endereco_serializer.save()
            professor = Professor.objects.create(endereco=endereco, **validated_data)
        else:
            # Se nenhum endereço for enviado, criamos o professor sem endereço
            professor = Professor.objects.create(**validated_data)

        return professor

    def validate(self, data):
        # Validação personalizada: só valida o endereço se ele for passado
        endereco_data = data.get('endereco')
        if endereco_data:
            # Validamos o serializer do endereço apenas se houver dados
            endereco_serializer = EnderecoSerializer(data=endereco_data)
            endereco_serializer.is_valid(raise_exception=True)
        return data

class AdministradorSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(required=False, allow_null=True)  # Endereco é opcional

    class Meta:
        model = Administrador
        fields = ['id', 'full_name', 'departamento', 'email', 'cpf', 'escola', 'data_inscricao', 'telefone_1',
                  'telefone_2', 'endereco']

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco', None)  # Remove o campo endereco se não existir

        if endereco_data:
            # Se houver dados de endereço, validamos e criamos o endereço
            endereco_serializer = EnderecoSerializer(data=endereco_data)
            endereco_serializer.is_valid(raise_exception=True)  # Valida apenas se houver dados de endereço
            endereco = endereco_serializer.save()
            administrador = Administrador.objects.create(endereco=endereco, **validated_data)
        else:
            # Se nenhum endereço for enviado, criamos o administrador sem endereço
            administrador = Administrador.objects.create(**validated_data)

        return administrador

    def validate(self, data):
        # Validação personalizada: só valida o endereço se ele for passado
        endereco_data = data.get('endereco')
        if endereco_data:
            # Validamos o serializer do endereço apenas se houver dados
            endereco_serializer = EnderecoSerializer(data=endereco_data)
            endereco_serializer.is_valid(raise_exception=True)
        return data
