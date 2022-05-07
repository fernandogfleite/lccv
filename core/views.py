from rest_framework import (
    viewsets,
    status
)
from rest_framework.response import Response

from django.db.models import ProtectedError
from django.contrib.auth import get_user_model

from core.models import (
    Cidade,
    Conta,
    Endereco,
    Ocorrencia,
    Pessoa,
    Uf
)
from core.serializers import (
    CidadeSerializer,
    ContaSerializer,
    EnderecoSerializer,
    OcorrenciaSerializer,
    PessoaSerializer,
    UfSerializer,
    UserSerializer
)


User = get_user_model()


class DestroyProtecedMixin:
    def destroy(self, request, *args, **kwargs):
        error = 'This instance is being used, so it is not possible to delete.'
        try:
            return super().destroy(request, *args, **kwargs)

        except ProtectedError:
            return Response(
                {
                    'error': error
                }, status=status.HTTP_400_BAD_REQUEST
            )


class UserViewSet(DestroyProtecedMixin,
                  viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UfViewSet(DestroyProtecedMixin,
                viewsets.ModelViewSet):
    serializer_class = UfSerializer
    queryset = Uf.objects.all()


class CidadeViewSet(DestroyProtecedMixin,
                    viewsets.ModelViewSet):
    serializer_class = CidadeSerializer
    queryset = Cidade.objects.all()


class EnderecoViewSet(DestroyProtecedMixin,
                      viewsets.ModelViewSet):
    serializer_class = EnderecoSerializer
    queryset = Endereco.objects.all()


class ContaViewSet(DestroyProtecedMixin,
                   viewsets.ModelViewSet):
    serializer_class = ContaSerializer
    queryset = Conta.objects.all()


class PessoaViewSet(DestroyProtecedMixin,
                    viewsets.ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = Pessoa.objects.all()


class OcorrenciaViewSet(DestroyProtecedMixin,
                        viewsets.ModelViewSet):
    serializer_class = OcorrenciaSerializer
    queryset = Ocorrencia.objects.all()
