from django.db import models
from django.db.models.deletion import DO_NOTHING
from stdimage.models import StdImageField


class Base(models.Model):
    """ A classe BASE é uma class abstrata e não é criada no banco de addos
    servirá apenas de rascunho para outras classes. """

    # Só adiciona a Data na criação do objeto
    DataCriacao = models.DateField(
        verbose_name='Data de Criação', auto_now_add=True)
    # Adiciona a data Em toda alteração
    DataAlteracao = models.DateField(
        verbose_name='Data de Alteração', auto_now=True)
    Ativo = models.BooleanField(default=True, verbose_name='Ativo?')

    class Meta:
        abstract = True


class Categoria(Base):
    NomeCategoria = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return self.NomeCategoria


class Servico(models.Model):
    NomeServico = models.CharField(
        max_length=35, verbose_name='Nome do Serviço')
    DescricaoServico = models.CharField(
        max_length=255, verbose_name='Descrição')
    FkCategoria = models.ForeignKey(
        'core.Categoria', verbose_name='Categoria', on_delete=models.DO_NOTHING)
    ImageServico = StdImageField(
        'Image', upload_to='servicos/images', variations={'thumb': {'width': 400, 'height': 400, 'crop': True}})
    SlugServico = models.SlugField(
        max_length=150, blank=True, editable=False, verbose_name='Slug')
    Instagram = models.CharField(max_length=255, null=True, blank=True, verbose_name='Instagram')
    Facebook = models.CharField(max_length=255, null=True, blank=True, verbose_name='Facebook')

    class Meta:
        verbose_name = ("Serviço")
        verbose_name_plural = ("Serviços")

    def __str__(self):
        return self.NomeServico
