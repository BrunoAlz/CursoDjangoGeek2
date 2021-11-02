from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class ErrorView(TemplateView):
    template_name = 'parciais/_404.html'