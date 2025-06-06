# Generated by Django 5.2 on 2025-04-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_project_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created'], 'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AddField(
            model_name='project',
            name='git_hub',
            field=models.URLField(blank=True, null=True, verbose_name='Repositorio de Git Hub'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='fecha de modificación'),
        ),
    ]
