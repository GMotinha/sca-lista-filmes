# Generated by Django 4.1.2 on 2022-11-26 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0004_filme_premio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filme',
            name='premio',
        ),
    ]
