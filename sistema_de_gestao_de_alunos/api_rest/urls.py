from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Crie um ViewSet para o modelo User
router = DefaultRouter()
router.register(r'users', UserViewSet)

# URLs
urlpatterns = [
    path('', include(router.urls)),
]
