# Generated by Django 4.0.5 on 2022-07-01 13:55

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_cursos_fotos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cursos',
            options={'ordering': ['created'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
                ('coment', ckeditor.fields.RichTextField(verbose_name='Comentario')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.cursos', verbose_name='Curso')),
            ],
            options={
                'verbose_name': 'Comentarios',
                'ordering': ['-created'],
            },
        ),
    ]