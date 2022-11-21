from django.views.generic import TemplateView, ListView
from .models import Filme


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['filme'] = Filme.objects.order_by('?').all()
        return context


class FilmeDetalheView(ListView):
    template_name = 'filme-area.html'
    paginate_by = 5
    ordering = 'nome'
    model = Filme

    def get_context_data(self, **kwargs):
        context = super(FilmeDetalheView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['filme'] = Filme.objects.filter(id=id).first
        return context

    def get_queryset(self, **kwargs):
        id = self.kwargs['id']
        return Filme.objects.filter(filme_id=id)
