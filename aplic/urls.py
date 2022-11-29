from django.urls import path

from .views import IndexView, SobreView, FilmeView
from .views import RelatoriofilmeView
from .views import FilmedetalhesView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about-us', SobreView.as_view(), name='sobre'),
    path('relatorio-filmes/', RelatoriofilmeView.as_view(), name='relatorio-filmes'),
    path('filme-details/<int:id>/', FilmedetalhesView.as_view(), name='filme-detalhes'),
    path('filme', FilmeView.as_view(), name='filme'),
]

