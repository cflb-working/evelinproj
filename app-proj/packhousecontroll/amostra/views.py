from rest_framework import viewsets
from .models import Amostra
from .serializers import AmostraSerializer


class AmostraViewSet(viewsets.ModelViewSet):
    queryset = Amostra.objects.all()
    serializer_class = AmostraSerializer
