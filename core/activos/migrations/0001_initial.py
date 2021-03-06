# Generated by Django 3.1.7 on 2021-03-10 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='Nombre')),
                ('impacto', models.TextField(verbose_name='Impacto')),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now, verbose_name='Timestamp')),
                ('vulnerabilidades', models.TextField(verbose_name='Vulnerabilidades')),
            ],
            options={
                'verbose_name': 'Activo',
                'verbose_name_plural': 'Activos',
                'db_table': 'activo',
                'ordering': ['id'],
            },
        ),
    ]
