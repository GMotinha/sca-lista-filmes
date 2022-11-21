from django.contrib import admin
from .models import Atores, Filme, Serie, Documentario, Genero, Premio

@admin.register(Atores)
class AtoresAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo')

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'duracao', 'sinopse', 'data_lancamento', 'ator')

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('nome_serie', 'sinopse', 'duracao', 'data_lancamento', 'ator')

@admin.register(Documentario)
class DocumentarioAdmin(admin.ModelAdmin):
    list_display = ('nome_documentario', 'sinopse', 'duracao', 'data_lancamento', 'ator')

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ()

@admin.register(Premio)
class Premio(admin.ModelAdmin):
    list_display = ()