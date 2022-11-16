from django.db import models

class Frentista(models.Model):
    nome = models.CharField('Nome', max_length=50)
    cpf = models.CharField('CPF', max_length=11)
    posto = models.CharField('Posto', max_length=50)

    class Meta:
        verbose_name = 'Frentista'
        verbose_name_plural = 'Frentistas'


class Bico:
    tipo_bico = models.CharField('Bicos')

    class Meta:
        verbose_name = 'Bico'
        verbose_name_plural = 'Bicos'

class Venda(Bico):
    total_venda = models.CharField('Valor da venda')

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

class Litragem:
    estoque_inicial = models.IntegerField('Estoque Inicial')
    estoque_final = models.IntegerField('Estoque Final')

    class Meta:
        verbose_name = 'Litragem'
        verbose_name_plural = 'Litragens'

class Combustivel(Litragem):
    OPCOES = (
        ('Gasolina Comum', 'Gasolina Comum'),
        ('Gasolina Aditivada', 'Gasolina Aditivada'),
        ('Diesel', 'Diesel'),
    )
    combustivel = models.CharField('Combustível', blank=True, choices=OPCOES)

    class Meta:
        verbose_name = 'Combustivel'
        verbose_name_plural = 'Combustiveis'

class Preco(models.Model):
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=3)

    class Meta:
        verbose_name = 'Preco'
        verbose_name_plural = 'Precos'

class Bomba(models.Model):
    tipo_bomba = models.CharField('Tipo de Bomba', max_length=100)

    class Meta:
        verbose_name = 'Bomba'
        verbose_name_plural = 'Bombas'