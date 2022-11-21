from django.urls import path

from .views import IndexView
from .views import RelatoriofilmeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('relatorio-filmes/', RelatoriofilmeView.as_view(), name='relatorio-filmes'),
]
