from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from core import models


User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                'fields': ('first_name', 'last_name'),
                'classes': ('wide',)
            }
        ),
    )


class CidadeAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Cidade


class UfAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Uf


class EnderecoAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Endereco


class ContaAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Conta


class PessoaAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Pessoa


class OcorrenciaAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Ocorrencia


admin.site.register(models.Cidade, CidadeAdmin)
admin.site.register(models.Uf, UfAdmin)
admin.site.register(models.Endereco, EnderecoAdmin)
admin.site.register(models.Conta, ContaAdmin)
admin.site.register(models.Pessoa, PessoaAdmin)
admin.site.register(models.Ocorrencia, OcorrenciaAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
