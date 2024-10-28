# Generated by Django 5.0.6 on 2024-09-18 00:00

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.IntegerField()),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('TI', 'Tarjeta de identidad')], default='CC', max_length=100)),
                ('fecha_nacimiento', models.DateField(default=datetime.date.today)),
                ('nombre_empleado', models.CharField(max_length=200)),
                ('apellido_empleado', models.CharField(max_length=100)),
                ('email_empleado', models.EmailField(max_length=50)),
                ('edad_empleado', models.IntegerField()),
                ('genero_empleado', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], max_length=80)),
                ('telefono_empleado', models.IntegerField(blank=True, null=True)),
                ('nit_empresa', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_contratacion', models.DateField(blank=True, null=True)),
                ('tipo_empleado', models.CharField(blank=True, choices=[('Dependiente', 'Dependiente'), ('Independiente', 'Independiente')], max_length=200, null=True)),
                ('nivel_riesgo', models.CharField(blank=True, choices=[('Uno', 'Uno'), ('Dos', 'Dos'), ('Tres', 'Tres'), ('Cuatro', 'Cuatro'), ('Cinco', 'Cinco')], max_length=200, null=True)),
                ('salario_empleado', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('foto_empleado', models.ImageField(blank=True, null=True, upload_to='fotos_empleados/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'empleados',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SeguridadSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salud', models.IntegerField(blank=True, null=True)),
                ('pension', models.IntegerField(blank=True, null=True)),
                ('caja_compensacion', models.IntegerField(blank=True, null=True)),
                ('arl', models.IntegerField(blank=True, null=True)),
                ('cesantias', models.IntegerField(blank=True, null=True)),
                ('interes_cesantias', models.IntegerField(blank=True, null=True)),
                ('prima', models.IntegerField(blank=True, null=True)),
                ('fecha_actual', models.DateField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.empleado')),
            ],
        ),
    ]
