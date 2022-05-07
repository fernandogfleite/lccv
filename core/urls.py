from django.urls import (
    include,
    path
)
from rest_framework.routers import DefaultRouter

from core.views import (
    UfViewSet,
    UserViewSet,
    CidadeViewSet,
    EnderecoViewSet,
    ContaViewSet,
    PessoaViewSet,
    OcorrenciaViewSet
)


router = DefaultRouter()

router.register('ufs', UfViewSet)
router.register('users', UserViewSet)
router.register('cidades', CidadeViewSet)
router.register('enderecos', EnderecoViewSet)
router.register('contas', ContaViewSet)
router.register('pessoas', PessoaViewSet)
router.register('ocorrencias', OcorrenciaViewSet)


app_name = 'core'
urlpatterns = [
    path('', include(router.urls))
]
