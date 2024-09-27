from rest_framework.serializers import ModelSerializer

from core.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TrabalhadorPequeno(ModelSerializer):
    class Meta:
        model = User
        fields = ("foto", "nome", "nota", "categoria")


class CategoriaTrabalhador(ModelSerializer):
    class Meta:
        model = User
        fields = "categoria"
