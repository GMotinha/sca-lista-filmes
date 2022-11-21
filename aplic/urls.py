from django.urls import path

from .views import IndexView
from .views import FilmeDetalheView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('filme-details/', FilmeDetalheView.as_view(), name='filme-detalhes'),
]
