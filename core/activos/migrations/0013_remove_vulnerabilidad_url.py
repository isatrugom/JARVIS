# Generated by Django 3.1.7 on 2021-05-17 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0012_auto_20210517_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vulnerabilidad',
            name='url',
        ),
    ]
