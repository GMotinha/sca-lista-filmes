# Generated by Django 4.1.2 on 2022-11-20 22:38

import aplic.models
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_documentario', models.CharField(max_length=100, verbose_name='Nome')),
                ('sinopse', models.TextField(max_length=500, verbose_name='Sinopse')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 260, 'width': 420}}, verbose_name='Imagem')),
                ('duracao', models.IntegerField(verbose_name='Duracação')),
                ('data_lancamento', models.DateField(blank=True, help_text='Formato DD/MM/AAAA', null=True, verbose_name='Data de Lançamento')),
            ],
            options={
                'verbose_name': 'Documentario',
                'verbose_name_plural': 'Documentarios',
            },
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sinopse', models.TextField(max_length=500, verbose_name='Sinopse')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 260, 'width': 420}}, verbose_name='Imagem')),
                ('duracao', models.IntegerField(verbose_name='Duracação')),
                ('data_lancamento', models.DateField(blank=True, help_text='Formato DD/MM/AAAA', null=True, verbose_name='Data de Lançamento')),
            ],
            options={
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('foto', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Ator',
                'verbose_name_plural': 'Atores',
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_serie', models.CharField(max_length=100, verbose_name='Nome')),
                ('sinopse', models.TextField(max_length=500, verbose_name='Sinopse')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 260, 'width': 420}}, verbose_name='Imagem')),
                ('duracao', models.IntegerField(verbose_name='Duracação')),
                ('data_lancamento', models.DateField(blank=True, help_text='Formato DD/MM/AAAA', null=True, verbose_name='Data de Lançamento')),
            ],
            options={
                'verbose_name': 'Serie',
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='Atores',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplic.pessoa')),
                ('sexo', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('teste', 'teste')], max_length=100, verbose_name='Sexo')),
            ],
            options={
                'verbose_name': 'Ator',
                'verbose_name_plural': 'Atores',
            },
            bases=('aplic.pessoa',),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, choices=[('Terror', 'Terror'), ('Suspense', 'Suspense'), ('Ação', 'Ação'), ('Desenho animado', 'Desenho animado')], max_length=100, verbose_name='Categoria')),
                ('documentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.documentario')),
                ('filme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.filme')),
                ('serie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.serie')),
            ],
        ),
        migrations.AddField(
            model_name='serie',
            name='ator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.atores'),
        ),
        migrations.AddField(
            model_name='filme',
            name='ator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.atores'),
        ),
        migrations.AddField(
            model_name='documentario',
            name='ator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.atores'),
        ),
    ]
