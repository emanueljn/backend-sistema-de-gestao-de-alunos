from django.contrib.auth.models import User
from rest_framework import serializers

# Defina um serializer para o modelo User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'