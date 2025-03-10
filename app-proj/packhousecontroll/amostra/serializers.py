from rest_framework import serializers
from .models import PadraoCor, Maturacao, Calibre, CalibresAmostra, DanosDetectados, Amostra

class AmostraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amostra
        fields = '__all__'

class PadraoCorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PadraoCor
        fields = '__all__'

class MaturacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maturacao
        fields = '__all__'

class CalibreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calibre
        fields = '__all__'

class CalibresAmostraSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalibresAmostra
        fields = '__all__'

class DanosDetectadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanosDetectados
        fields = '__all__'
