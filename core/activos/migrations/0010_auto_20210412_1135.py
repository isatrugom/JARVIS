# Generated by Django 3.1.7 on 2021-04-12 09:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0009_auto_20210412_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plugin',
            name='id',
        ),
        migrations.RemoveField(
            model_name='plugin',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='protocolo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='protocolo',
            name='nombre',
        ),
        migrations.AddField(
            model_name='plugin',
            name='activo_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activos.activo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='protocolo',
            name='activo_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activos.activo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exploit',
            name='activo',
            field=models.ManyToManyField(blank=True, to='activos.Activo'),
        ),
        migrations.AlterField(
            model_name='ordenador',
            name='datos',
            field=models.ManyToManyField(blank=True, to='activos.Datos'),
        ),
        migrations.AlterField(
            model_name='ordenador',
            name='software',
            field=models.ManyToManyField(blank=True, to='activos.Software'),
        ),
        migrations.AlterField(
            model_name='plugin',
            name='fechaAdquisicion',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de adquisición'),
        ),
        migrations.AlterField(
            model_name='plugin',
            name='protocolo',
            field=models.ManyToManyField(blank=True, to='activos.Protocolo'),
        ),
        migrations.AlterField(
            model_name='protocolo',
            name='puerto',
            field=models.ManyToManyField(blank=True, to='activos.Puerto'),
        ),
        migrations.AlterField(
            model_name='software',
            name='datos',
            field=models.ManyToManyField(blank=True, to='activos.Datos'),
        ),
        migrations.AlterField(
            model_name='software',
            name='fechaAdquisicion',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de adquisición'),
        ),
        migrations.AlterField(
            model_name='software',
            name='plugin',
            field=models.ManyToManyField(blank=True, to='activos.Plugin'),
        ),
        migrations.AlterField(
            model_name='vulnerabilidad',
            name='activo',
            field=models.ManyToManyField(blank=True, to='activos.Activo'),
        ),
        migrations.AlterField(
            model_name='vulnerabilidad',
            name='exploit',
            field=models.ManyToManyField(blank=True, to='activos.Exploit'),
        ),
    ]
