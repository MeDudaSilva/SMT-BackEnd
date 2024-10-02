from rest_framework.serializers import ModelSerializer, CharField

from core.models import User


class TrabalhadorPequeno(ModelSerializer):
    class Meta:
        model = User
        fields = ("foto", "name", "categoria")

class UserSerializer(ModelSerializer):
    foto = CharField(source='foto.url', read_only=True)
    class Meta:
        model = User
        fields = "__all__"
