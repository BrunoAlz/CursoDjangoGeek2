from django.contrib import admin
from .models import Categoria, Servico


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'NomeCategoria', 'Ativo', 'DataCriacao', 'DataAlteracao')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('NomeServico', 'DescricaoServico', 'FkCategoria', 'Ativo', 'DataCriacao',)
