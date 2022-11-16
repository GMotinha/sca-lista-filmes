from django.contrib import admin
from .models import Frentista, Venda, Bico, Combustivel, Preco, Litragem, Bomba

@admin.register(Frentista)
class FrentistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = 'total_venda'

@admin.register(Bico)
class BicoAdmin(admin.ModelAdmin):
    list_display = ('combustivel', 'preco_bico')

@admin.register(Combustivel)
class CombustivelAdmin(admin.ModelAdmin):
    list_display = 'combustivel'

@admin.register(Preco)
class PrecoAdmin(admin.ModelAdmin):
    list_display = 'valor'

@admin.register(Litragem)
class LitragemAdmin(admin.ModelAdmin):
    list_display = ('estoque Inicial', 'estoque Final')

@admin.register(Bomba)
class BombaAdmin(admin.ModelAdmin):
    list_display = 'Tipo de Bomba'
