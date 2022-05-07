
from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import (
    Cidade,
    Conta,
    Endereco,
    Ocorrencia,
    Pessoa,
    Uf
)


User = get_user_model()


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name'
        )


class UfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uf
        fields = '__all__'


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        uf_serializer = UfSerializer(
            instance=instance.uf
        )

        data['uf'] = uf_serializer.data

        return data


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        cidade_serializer = CidadeSerializer(
            instance=instance.cidade
        )

        data['cidade'] = cidade_serializer.data

        return data


class ContaSerializer(serializers.ModelSerializer):
    tipo = ChoiceField(choices=Conta.TIPOS)
    banco = ChoiceField(choices=Conta.BANCOS)

    class Meta:
        model = Conta
        fields = '__all__'


class PessoaSerializer(serializers.ModelSerializer):
    vinculo = ChoiceField(choices=Pessoa.VINCULOS)

    class Meta:
        model = Pessoa
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        user_serializer = UserSerializer(
            instance=instance.user
        )
        endereco_serializer = EnderecoSerializer(
            instance=instance.endereco
        )
        conta_serializer = ContaSerializer(
            instance=instance.conta
        )

        data['user'] = user_serializer.data
        data['endereco'] = endereco_serializer.data
        data['conta'] = conta_serializer.data

        return data


class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['pessoa'] = dict(
            id=instance.pessoa.id,
            nome=instance.pessoa.nome
        )

        return data
