from rest_framework.serializers import ModelSerializer

from core.models import Trabalho


class TrabalhoSerializer(ModelSerializer):
    class Meta:
        model = Trabalho
        fields = "__all__"
