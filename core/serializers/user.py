from rest_framework.serializers import CharField, ModelSerializer

from core.models import User


class TrabalhadorPequeno(ModelSerializer):
    class Meta:
        model = User
        fields = ("foto", "name", "categoria", "tipo")


class UserSerializer(ModelSerializer):
    foto = CharField(source="foto.url", read_only=True)

    class Meta:
        model = User
        fields = "__all__"


class PerfilSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "foto", "capa", "publicacao", "publicacaoFoto", "descricao")
