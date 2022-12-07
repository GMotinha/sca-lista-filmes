from django.contrib import admin
from .models import Diretor, Filme, Serie, Documentario, Genero

@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo')


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'duracao', 'sinopse', 'data_lancamento', 'diretor')


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('nome_serie', 'sinopse', 'duracao', 'data_lancamento', 'diretor')


@admin.register(Documentario)
class DocumentarioAdmin(admin.ModelAdmin):
    list_display = ('nome_documentario', 'sinopse', 'duracao', 'data_lancamento', 'diretor')
