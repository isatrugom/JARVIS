# Generated by Django 3.1.7 on 2021-04-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0004_auto_20210406_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='software',
            name='plugin',
        ),
        migrations.AddField(
            model_name='software',
            name='plugin',
            field=models.ManyToManyField(to='activos.Plugin'),
        ),
    ]
