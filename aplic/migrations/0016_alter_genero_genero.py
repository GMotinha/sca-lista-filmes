# Generated by Django 4.1.2 on 2022-12-07 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0015_alter_serie_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='genero',
            field=models.TextField(blank=True, max_length=100, verbose_name='Categoria'),
        ),
    ]