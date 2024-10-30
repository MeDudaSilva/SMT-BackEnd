from rest_framework.viewsets import ModelViewSet

from core.models import Trabalho
from core.serializers import (
    ClienteAvaliacaoSerializer,
    HistoricoTrabalhoSerializer,
    TrabalhadorAvaliacaoSerializer,
    TrabalhoSerializer,
)


class TrabalhoViewSet(ModelViewSet):
    queryset = Trabalho.objects.all()
    serializer_class = TrabalhoSerializer


class HistoricoTrabalhoViewSet(ModelViewSet):
    queryset = Trabalho.objects.all()
    serializer_class = HistoricoTrabalhoSerializer


class AvalicaoTrabalhadorViewSet(ModelViewSet):
    queryset = Trabalho.objects.all()
    serializer_class = TrabalhadorAvaliacaoSerializer


class AvalicaoClienteViewSet(ModelViewSet):
    queryset = Trabalho.objects.all()
    serializer_class = ClienteAvaliacaoSerializer
