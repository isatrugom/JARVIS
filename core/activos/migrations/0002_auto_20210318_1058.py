# Generated by Django 3.1.7 on 2021-03-18 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('activo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activos.activo')),
                ('ubicacion', models.TextField(verbose_name='Ubicación')),
                ('local', models.BooleanField(verbose_name='Local')),
            ],
            options={
                'verbose_name': 'Dato',
                'verbose_name_plural': 'Datos',
                'db_table': 'dato',
                'ordering': ['id'],
            },
            bases=('activos.activo',),
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('activo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activos.activo')),
                ('modelo', models.TextField(verbose_name='Modelo')),
                ('proveedor', models.TextField(verbose_name='Proveedor')),
                ('numeroDeSerie', models.TextField(verbose_name='Número de Serie')),
                ('tipoHardware', models.CharField(choices=[('P', 'Periférico'), ('SERV', 'Servidor'), ('SEN', 'Sensor'), ('A', 'Actuador'), ('O', 'Ordenador'), ('ND', 'No determinado'), ('ER', 'Equipo de red'), ('S', 'Smartphone')], max_length=4, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Hardware',
                'verbose_name_plural': 'Hardware',
                'db_table': 'hardware',
                'ordering': ['id'],
            },
            bases=('activos.activo',),
        ),
        migrations.CreateModel(
            name='Humano',
            fields=[
                ('activo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activos.activo')),
                ('puesto', models.TextField(verbose_name='Puesto')),
            ],
            options={
                'verbose_name': 'Humano',
                'verbose_name_plural': 'Humanos',
                'db_table': 'humano',
                'ordering': ['id'],
            },
            bases=('activos.activo',),
        ),
        migrations.CreateModel(
            name='NoDeterminado',
            fields=[
                ('activo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activos.activo')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('detalles', models.TextField(verbose_name='Detalles')),
            ],
            options={
                'verbose_name': 'No determinado',
                'verbose_name_plural': 'No determinados',
                'db_table': 'noDeterminado',
                'ordering': ['id'],
            },
            bases=('activos.activo',),
        ),
        migrations.CreateModel(
            name='Nube',
            fields=[
                ('activo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activos.activo')),
                ('url', models.TextField(verbose_name='URL')),
                ('dominio', models.TextField(verbose_name='Dominio')),
            ],
            options={
                'verbose_name': 'Nube',
                'verbose_name_plural': 'Nube',
                'db_table': 'nube',
                'ordering': ['id'],
            },
            bases=('activos.activo',),
        ),
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='Nombre')),
                ('version', models.TextField(verbose_name='Versión')),
                ('proveedor', models.TextField(verbose_name='Proveedor')),
                ('fechaAdquisicion', models.DateTimeField(verbose_name='Fecha de adquisición')),
                ('fechaExpiracion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de expiración')),
            ],
            options={
                'verbose_name': 'Plugin',
                'verbose_name_plural': 'Plugins',
                'db_table': 'plugin',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Puerto',
            fields=[
                ('activo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activos.activo')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('estado', models.CharField(choices=[('A', 'Abiero'), ('C', 'Cerrado'), ('F', 'Filtrado')], max_length=1, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Puerto',
                'verbose_name_plural': 'Puertos',
                'db_table': 'puerto',
                'ordering': ['numero'],
            },
            bases=('activos.activo',),
        ),
        migrations.CreateModel(
            name='Red',
            fields=[
                ('activo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activos.activo')),
                ('cidr', models.TextField(verbose_name='Bloque CIDR')),
                ('nat', models.BooleanField(verbose_name='NAT')),
            ],
            options={
                'verbose_name': 'Red',
                'verbose_name_plural': 'Redes',
                'db_table': 'red',
                'ordering': ['id'],
            },
            bases=('activos.activo',),
        ),
        migrations.RemoveField(
            model_name='activo',
            name='vulnerabilidades',
        ),
        migrations.AlterField(
            model_name='activo',
            name='impacto',
            field=models.CharField(choices=[('A', 'Alto'), ('M', 'Medio'), ('B', 'Bajo')], max_length=1, verbose_name='Impacto'),
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('activo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activos.activo')),
                ('version', models.TextField(verbose_name='Versión')),
                ('proveedor', models.TextField(verbose_name='Proveedor')),
                ('fechaAdquisicion', models.DateTimeField(verbose_name='Fecha de adquisición')),
                ('fechaExpiracion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de expiración')),
                ('tipoSoftware', models.CharField(choices=[('S', 'Sistema operativo'), ('F', 'Firmware'), ('A', 'Antivirus'), ('AM', 'Aplicación Móvil'), ('C', 'Código')], max_length=2, verbose_name='Tipo')),
                ('datos', models.ManyToManyField(to='activos.Datos')),
                ('plugin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.plugin')),
            ],
            options={
                'verbose_name': 'Software',
                'verbose_name_plural': 'Softwares',
                'db_table': 'software',
                'ordering': ['id'],
            },
            bases=('activos.activo',),
        ),
        migrations.CreateModel(
            name='Protocolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='Nombre')),
                ('version', models.TextField(verbose_name='Versión')),
                ('puerto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.puerto')),
            ],
            options={
                'verbose_name': 'Protocolo',
                'verbose_name_plural': 'Protocolos',
                'db_table': 'protocolo',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='plugin',
            name='protocolo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.protocolo'),
        ),
        migrations.CreateModel(
            name='Ordenador',
            fields=[
                ('hardware_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activos.hardware')),
                ('ram', models.IntegerField(verbose_name='Memoria RAM')),
                ('rom', models.IntegerField(verbose_name='Memoria ROM')),
                ('nucleos', models.IntegerField(verbose_name='Número de núcleos')),
                ('datos', models.ManyToManyField(to='activos.Datos')),
                ('software', models.ManyToManyField(to='activos.Software')),
            ],
            options={
                'verbose_name': 'Ordenador',
                'verbose_name_plural': 'Ordenadores',
                'db_table': 'ordenador',
                'ordering': ['id'],
            },
            bases=('activos.hardware',),
        ),
        migrations.CreateModel(
            name='EquipoRed',
            fields=[
                ('hardware_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activos.hardware')),
                ('tipoEquipo', models.CharField(choices=[('G', 'Gateway'), ('I', 'Interfaz'), ('R', 'Router'), ('S', 'Switch')], max_length=1, verbose_name='Tipo')),
                ('redAsociada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.red')),
            ],
            options={
                'verbose_name': 'Equipo de red',
                'verbose_name_plural': 'Equipos de red',
                'db_table': 'equipo_red',
                'ordering': ['id'],
            },
            bases=('activos.hardware',),
        ),
    ]