from django.urls import path

from .views import IndexView, SobreView, FilmeView, SerieView
from .views import RelatoriofilmeView, RelatorioserieView, RelatoriodocumentarioView
from .views import FilmedetalhesView, SeriedetalhesView
from .views import DadosGraficoFilmesView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about-us', SobreView.as_view(), name='sobre'),
    path('relatorio-filmes/', RelatoriofilmeView.as_view(), name='relatorio-filmes'),
    path('filme-details/<int:id>/', FilmedetalhesView.as_view(), name='filme-detalhes'),
    path('filme', FilmeView.as_view(), name='filme'),
    path('relatorio-series/', RelatorioserieView.as_view(), name='relatorio-series'),
    path('relatorio-documentarios/', RelatoriodocumentarioView.as_view(), name='relatorio-documentarios'),
    path('serie', SerieView.as_view(), name='serie'),
    path('serie-details/<int:id>/', SeriedetalhesView.as_view(), name='serie-detalhes'),
    path('dados-grafico-filmes/', DadosGraficoFilmesView.as_view(), name='dados-grafico-filmes'),


]

