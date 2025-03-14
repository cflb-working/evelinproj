from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AmostraViewSet #, PadraoCorViewSet, CalibreViewSet

router = DefaultRouter()
router.register(r'amostras', AmostraViewSet)
# router.register(r'padroes_cor', PadraoCorViewSet)
# router.register(r'calibres', CalibreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
