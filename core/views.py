from django.views.generic import TemplateView
from .models import Categoria, Servico


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['servicos'] = Servico.objects.all()
        return context


class ErrorView(TemplateView):
    template_name = 'parciais/_404.html'
