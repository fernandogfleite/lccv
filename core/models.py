from django.db import models


class Uf(models.Model):
    nome = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )
    sigla = models.CharField(
        max_length=2,
        blank=False,
        null=False
    )

    class Meta:
        db_table = "ufs"


class Cidade(models.Model):
    nome = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    uf = models.ForeignKey(
        "core.Uf",
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )

    class Meta:
        db_table = "cidades"


class Endereco(models.Model):
    cidade = models.ForeignKey(
        "core.Cidade",
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    logradouro = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )
    numero = models.CharField(
        verbose_name="Número",
        max_length=8,
        blank=False,
        null=False
    )
    cep = models.CharField(
        max_length=10,
        blank=False,
        null=False
    )
    bairro = models.CharField(
        max_length=80,
        blank=False,
        null=False
    )
    complemento = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )
    observacoes = models.TextField(
        verbose_name="Observações",
        blank=True,
        null=True
    )

    class Meta:
        db_table = "enderecos"


class Conta(models.Model):
    POUPANCA = "Poupança"
    CORRENTE = "Corrente"

    TIPOS = (
        (POUPANCA, "Poupança"),
        (CORRENTE, "Corrente")
    )

    BANCO_1 = "Banco 1"
    BANCO_2 = "Banco 2"
    BANCO_3 = "Banco 3"
    BANCO_4 = "Banco 4"

    BANCOS = (
        (BANCO_1, "Banco 1"),
        (BANCO_2, "Banco 2"),
        (BANCO_3, "Banco 3"),
        (BANCO_4, "Banco 4")
    )

    tipo = models.CharField(
        max_length=30,
        choices=TIPOS,
        blank=False,
        null=False
    )
    banco = models.CharField(
        max_length=50,
        choices=BANCOS,
        blank=False,
        null=False
    )
    conta = models.IntegerField(
        blank=False,
        null=False
    )
    agencia = models.IntegerField(
        verbose_name="Agência",
        blank=False,
        null=False
    )
    operacao = models.IntegerField(
        verbose_name="Operação",
        blank=False,
        null=False
    )

    class Meta:
        db_table = "contas"


class Pessoa(models.Model):
    VINCULO_1 = "Vinculo 1"
    VINCULO_2 = "Vinculo 2"

    VINCULOS = (
        (VINCULO_1, "Vinculo 1"),
        (VINCULO_2, "Vinculo 2")
    )

    vinculo = models.CharField(
        choices=VINCULOS,
        max_length=20,
        blank=False,
        null=False
    )
    user = models.OneToOneField(
        "auth.User",
        verbose_name="Usuário",
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    cpf = models.IntegerField(
        blank=False,
        null=False
    )
    nome = models.CharField(
        max_length=200,
        blank=False,
        null=False
    )
    telefone = models.CharField(
        max_length=16,
        blank=False,
        null=False
    )
    email = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    endereco = models.ForeignKey(
        "core.Endereco",
        verbose_name="Endereço",
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    conta = models.ForeignKey(
        "core.Conta",
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )

    class Meta:
        db_table = "pessoas"


class Ocorrencia(models.Model):
    data = models.DateField(
        blank=False,
        null=False
    )
    realizada = models.CharField(
        max_length=1,
        blank=False,
        null=False
    )
    ocorrencia = models.TextField(
        verbose_name="Ocorrência",
        blank=False,
        null=False
    )
    pessoa = models.ForeignKey(
        "core.Pessoa",
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )

    class Meta:
        db_table = "ocorrencias"
