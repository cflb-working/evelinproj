from django.contrib import admin
from .models import Calibre, Amostra, PadraoCor, CalibresAmostra, DanosDetectados, Maturacao

admin.site.register(Maturacao)
admin.site.register(Calibre)
admin.site.register(PadraoCor)
admin.site.register(CalibresAmostra)
admin.site.register(DanosDetectados)
admin.site.register(Amostra)
