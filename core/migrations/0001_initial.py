# Generated by Django 4.0.4 on 2022-05-05 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cidades',
            },
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Poupança', 'Poupança'), ('Corrente', 'Corrente')], max_length=30)),
                ('banco', models.CharField(choices=[('Banco 1', 'Banco 1'), ('Banco 2', 'Banco 2'), ('Banco 3', 'Banco 3'), ('Banco 4', 'Banco 4')], max_length=50)),
                ('conta', models.IntegerField()),
                ('agencia', models.IntegerField(verbose_name='Agência')),
                ('operacao', models.IntegerField(verbose_name='Operação')),
            ],
            options={
                'db_table': 'contas',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=150)),
                ('numero', models.CharField(max_length=8, verbose_name='Número')),
                ('cep', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=80)),
                ('complemento', models.CharField(blank=True, max_length=60, null=True)),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cidade')),
            ],
            options={
                'db_table': 'enderecos',
            },
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sigla', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'ufs',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vinculo', models.CharField(choices=[('Vinculo 1', 'Vinculo 1'), ('Vinculo 2', 'Vinculo 2')], max_length=20)),
                ('cpf', models.IntegerField()),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=255)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.conta')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.endereco', verbose_name='Endereço')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'db_table': 'pessoas',
            },
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('realizada', models.CharField(max_length=1)),
                ('ocorrencia', models.TextField(verbose_name='Ocorrência')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.pessoa')),
            ],
            options={
                'db_table': 'ocorrencias',
            },
        ),
        migrations.AddField(
            model_name='cidade',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.uf'),
        ),
    ]