from rest_framework.viewsets import ModelViewSet

from core.models import Trabalho
from core.serializers import TrabalhoSerializer


class TrabalhoViewSet(ModelViewSet):
    queryset = Trabalho.objects.all()
    serializer_class = TrabalhoSerializer
