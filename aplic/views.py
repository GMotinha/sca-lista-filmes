from django.views.generic import TemplateView, ListView
from django_weasyprint import WeasyTemplateView
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML

from .models import Filme

class IndexView(TemplateView):
    template_name = 'index.html'

class SobreView(TemplateView):
    template_name = 'about-us.html'

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['filmes'] = Filme.objects.order_by('nome').all()
        return context


class RelatoriofilmeView(WeasyTemplateView):

    def get(self, request, *args, **kwargs):
        filme = Filme.objects.order_by('nome').all()

        html_string = render_to_string('relatorio-filmes.html', {'filmes': filme})

        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        html.write_pdf(target='/tmp/relatorio-filmes.pdf')
        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio-filmes.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio-filmes.pdf"'
        return response


class FilmedetalhesView(ListView):
    template_name = 'filme-details.html'
    paginate_by = 5
    ordering = 'nome'
    model = Filme

    def get_context_data(self, **kwargs):
        context = super(FilmedetalhesView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['filme'] = Filme.objects.filter(id=id).first
        return context

    def get_queryset(self, **kwargs):
        id = self.kwargs['id']
        return Filme.objects.filter(filme_id=id)
