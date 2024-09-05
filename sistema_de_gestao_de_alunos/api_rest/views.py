from django.contrib.auth.models import User
from rest_framework import viewsets
from serializers import UserSerializer
from dj_rql.drf import RQLFilterBackend
from filters import UserFilterClass

# Crie um ViewSet para o modelo User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = UserFilterClass

