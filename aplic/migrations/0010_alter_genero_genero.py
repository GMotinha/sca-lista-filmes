# Generated by Django 4.1.2 on 2022-11-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0009_serie_episodios_serie_temporada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='genero',
            field=models.CharField(blank=True, choices=[('Terror', 'Terror'), ('Suspense', 'Suspense'), ('Ação', 'Ação'), ('Desenho animado', 'Desenho animado'), ('Drama', 'Drama')], max_length=100, verbose_name='Categoria'),
        ),
    ]