# Generated by Django 3.1.7 on 2021-04-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0005_auto_20210412_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exploit',
            name='activo',
            field=models.ManyToManyField(blank=True, null=True, to='activos.Activo'),
        ),
        migrations.AlterField(
            model_name='ordenador',
            name='datos',
            field=models.ManyToManyField(blank=True, null=True, to='activos.Datos'),
        ),
        migrations.AlterField(
            model_name='ordenador',
            name='software',
            field=models.ManyToManyField(blank=True, null=True, to='activos.Software'),
        ),
        migrations.AlterField(
            model_name='software',
            name='datos',
            field=models.ManyToManyField(blank=True, null=True, to='activos.Datos'),
        ),
        migrations.AlterField(
            model_name='software',
            name='plugin',
            field=models.ManyToManyField(blank=True, null=True, to='activos.Plugin'),
        ),
        migrations.AlterField(
            model_name='vulnerabilidad',
            name='activo',
            field=models.ManyToManyField(blank=True, null=True, to='activos.Activo'),
        ),
        migrations.AlterField(
            model_name='vulnerabilidad',
            name='exploit',
            field=models.ManyToManyField(blank=True, null=True, to='activos.Exploit'),
        ),
    ]