# Generated by Django 4.0.5 on 2022-06-27 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrecurso', models.CharField(max_length=12, verbose_name='Mat')),
                ('nombreprof', models.TextField()),
                ('duracion', models.TimeField()),
                ('evaluacion', models.TextField()),
                ('turno', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
