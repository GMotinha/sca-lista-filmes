from django.db import models
from stdimage.models import StdImageField
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path,
                         variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = 'Ator'
        verbose_name_plural = 'Atores'

    def __str__(self):
        return self.nome

class Atores(Pessoa):
    OPCOES = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('teste', 'teste'),
    )
    sexo = models.CharField('Sexo', blank=True, max_length=100, choices=OPCOES)

    class Meta:
        verbose_name = 'Ator'
        verbose_name_plural = 'Atores'

class Filme(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sinopse = models.TextField('Sinopse', max_length=500)
    imagem = StdImageField('Imagem', null=True, blank=True, upload_to=get_file_path,
                           variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})
    duracao = models.IntegerField('Duracação')
    data_lancamento = models.DateField('Data de Lançamento', blank=True, null=True, help_text='Formato DD/MM/AAAA')
    ator = models.ForeignKey(Atores, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
    def __str__(self):
        return self.nome

class Serie(models.Model):
        nome_serie = models.CharField('Nome', max_length=100)
        sinopse = models.TextField('Sinopse', max_length=500)
        imagem = StdImageField('Imagem', null=True, blank=True, upload_to=get_file_path,
                               variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})
        duracao = models.IntegerField('Duracação')
        data_lancamento = models.DateField('Data de Lançamento', blank=True, null=True, help_text='Formato DD/MM/AAAA')
        ator = models.ForeignKey(Atores, on_delete=models.CASCADE)

        class Meta:
            verbose_name = 'Serie'
            verbose_name_plural = 'Series'

        def __str__(self):
            return self.nome_serie

class Documentario(models.Model):
    nome_documentario = models.CharField('Nome', max_length=100)
    sinopse = models.TextField('Sinopse', max_length=500)
    imagem = StdImageField('Imagem', null=True, blank=True, upload_to=get_file_path,
                           variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})
    duracao = models.IntegerField('Duracação')
    data_lancamento = models.DateField('Data de Lançamento', blank=True, null=True, help_text='Formato DD/MM/AAAA')
    ator = models.ForeignKey(Atores, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Documentario'
        verbose_name_plural = 'Documentarios'

    def __str__(self):
        return self.nome_documentario


class Genero(models.Model):
    OPCOES = (
        ('Terror', 'Terror'),
        ('Suspense', 'Suspense'),
        ('Ação', 'Ação'),
        ('Desenho animado', 'Desenho animado'),
    )
    genero = models.CharField('Categoria', blank=True, max_length=100, choices=OPCOES)
    def __str__(self):
        return self.nome

class Premio (models.Model):
    OPCOES = (
        ('AFI Awards', 'AFI Awards'),
        ('Oscar', 'Oscar'),
        ('PGA', 'PGA'),
        ('BAFTA', 'BAFTA'),
    )
    premiacao = models.CharField('Premiações', blank=True, max_length=100, choices=OPCOES)