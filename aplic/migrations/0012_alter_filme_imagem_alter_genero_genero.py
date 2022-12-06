# Generated by Django 4.1.2 on 2022-11-29 20:09

import aplic.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0011_alter_genero_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='imagem',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 420, 'width': 420}}, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='genero',
            name='genero',
            field=models.CharField(blank=True, choices=[('Terror', 'Terror'), ('Suspense', 'Suspense'), ('Ação', 'Ação'), ('Desenho animado', 'Desenho animado'), ('Drama', 'Drama')], max_length=100, verbose_name='Categoria'),
        ),
    ]