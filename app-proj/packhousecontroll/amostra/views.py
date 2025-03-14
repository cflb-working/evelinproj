from rest_framework import viewsets
from .models import Amostra, PadraoCor, Calibre
from .serializers import AmostraSerializer, PadraoCorSerializer, CalibreSerializer


class AmostraViewSet(viewsets.ModelViewSet):
    queryset = Amostra.objects.all()
    serializer_class = AmostraSerializer


class PadraoCorViewSet(viewsets.ModelViewSet):
    queryset = PadraoCor.objects.all()
    serializer_class = PadraoCorSerializer

class CalibreViewSet(viewsets.ModelViewSet):
    queryset = Calibre.objects.all()
    serializer_class = CalibreSerializer