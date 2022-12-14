from django.views.generic import TemplateView, ListView
from django_weasyprint import WeasyTemplateView
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from django.db.models import Count
from chartjs.views.lines import BaseLineChartView

from .models import Filme, Serie, Documentario, Genero


class IndexView(TemplateView):
    template_name = 'index.html'


class SobreView(TemplateView):
    template_name = 'about-us.html'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['filmes'] = Filme.objects.order_by('nome').all()
        context['series'] = Serie.objects.order_by('nome_serie').all()
        return context


class FilmeView(TemplateView):
    template_name = 'filme.html'

    def get_context_data(self, **kwargs):
        context = super(FilmeView, self).get_context_data(**kwargs)
        context['filmes'] = Filme.objects.order_by('nome').all()
        return context


class SerieView(TemplateView):
    template_name = 'serie.html'

    def get_context_data(self, **kwargs):
        context = super(SerieView, self).get_context_data(**kwargs)
        context['series'] = Serie.objects.order_by('nome_serie').all()
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
    model = Genero

    def get_context_data(self, **kwargs):
        context = super(FilmedetalhesView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['filme'] = Filme.objects.filter(id=id).first
        return context

    def get_queryset(self, **kwargs):
        id = self.kwargs['id']
        return Genero.objects.filter(id=id)


class RelatorioserieView(WeasyTemplateView):
    def get(self, request, *args, **kwargs):
        serie = Serie.objects.order_by('nome_serie').all()

        html_string = render_to_string('relatorio-series.html', {'series': serie})

        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        html.write_pdf(target='/tmp/relatorio-series.pdf')
        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio-series.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio-series.pdf"'
        return response


class RelatoriodocumentarioView(WeasyTemplateView):
    def get(self, request, *args, **kwargs):
        documentario = Documentario.objects.order_by('nome_documentario').all()

        html_string = render_to_string('relatorio-documentarios.html', {'documentarios': documentario})

        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        html.write_pdf(target='/tmp/relatorio-documentarios.pdf')
        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio-documentarios.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio-documentarios.pdf"'
        return response


class SeriedetalhesView(ListView):
    template_name = 'serie-details.html'
    paginate_by = 5
    ordering = 'nome_serie'
    model = Serie

    def get_context_data(self, **kwargs):
        context = super(SeriedetalhesView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['serie'] = Serie.objects.filter(nome_serie=id).first
        return context

    def get_queryset(self, **kwargs):
        id = self.kwargs['id']
        return Serie.objects.filter(nome_serie=id)


class DadosGraficoFilmesView(BaseLineChartView):
    def get_labels(self):
        labels = []
        queryset = Filme.objects.order_by('diretor')
        for diretor in queryset:
            labels.append(diretor.nome)
        return labels

    def get_data(self):
        resultado = []
        dados = []
        queryset = Filme.objects.order_by('nome').annotate(total=Count('diretor'))
        for linha in queryset:
            dados.append(int(linha.total))
        resultado.append(dados)
        return resultado
