# Generated by Django 4.1.2 on 2022-11-29 20:26

import aplic.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0014_alter_filme_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='imagem',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 515, 'width': 350}}, verbose_name='Imagem'),
        ),
    ]
