from django.views.generic import TemplateView
from django_weasyprint import WeasyTemplateView
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML

from .models import Filme

class RelatoriofilmeView(WeasyTemplateView):

    def get(self, request, *args, **kwargs):
        filme = Filme.objects.order_by('nome').all()

        html_string = render_to_string('relatorio-filmes.html', {'alunos': filme})

        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        html.write_pdf(target='/tmp/relatorio-filmes.pdf')
        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio-filmes.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio-filmes.pdf"'
        return response

class IndexView(TemplateView):
    template_name = 'index.html'



