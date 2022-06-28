# Generated by Django 4.0.5 on 2022-06-28 00:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='update',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cursos',
            name='duracion',
            field=models.TextField(verbose_name='Duracion del curso'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='evaluacion',
            field=models.TextField(verbose_name='Tipo de evaluacion'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nombrecurso',
            field=models.CharField(max_length=12, verbose_name='Nombre del curso'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nombreprof',
            field=models.TextField(verbose_name='Nombre del profesor'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='turno',
            field=models.CharField(max_length=10, verbose_name='Turno en el que se imparte'),
        ),
    ]
