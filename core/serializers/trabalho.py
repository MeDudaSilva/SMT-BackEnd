from rest_framework.serializers import ModelSerializer

from core.models import Trabalho


class TrabalhoSerializer(ModelSerializer):
    class Meta:
        model = Trabalho
        fields = "__all__"

class HistóricoTrabalho(ModelSerializer):
    class Meta:
        model = Trabalho
        fields = ("nome", "DataDeTermino", "estado")
        depth = 1
