# Generated by Django 4.1.2 on 2022-11-29 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0007_documentario_genero_documentario_premio_serie_genero_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Atores',
            new_name='Diretor',
        ),
        migrations.AlterModelOptions(
            name='diretor',
            options={'verbose_name': 'Diretor', 'verbose_name_plural': 'Diretores'},
        ),
        migrations.AlterModelOptions(
            name='pessoa',
            options={'verbose_name': 'Diretor', 'verbose_name_plural': 'Diretores'},
        ),
        migrations.RenameField(
            model_name='documentario',
            old_name='ator',
            new_name='diretor',
        ),
        migrations.RenameField(
            model_name='filme',
            old_name='ator',
            new_name='diretor',
        ),
        migrations.RenameField(
            model_name='serie',
            old_name='ator',
            new_name='diretor',
        ),
    ]
