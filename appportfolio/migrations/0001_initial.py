# Generated by Django 4.1.5 on 2023-01-30 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(blank=True, max_length=30, null=True, verbose_name='Puesto de Trabajo')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nombre_categoria'],
            },
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('empresa', models.CharField(blank=True, max_length=50, null=True, verbose_name='Empresa')),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('fecha_fin', models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización')),
                ('observaciones', models.CharField(blank=True, max_length=50, null=True, verbose_name='Funciones')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='experiencias_categoria', to='appportfolio.categoria')),
            ],
            options={
                'verbose_name': 'Experiencia',
                'verbose_name_plural': 'Experiencias',
                'ordering': ['empresa'],
            },
        ),
    ]
