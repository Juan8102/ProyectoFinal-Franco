# Generated by Django 4.2.4 on 2023-08-04 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContentApp', '0002_imagen_delete_destacado_noticia_cuerpo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='imagen',
        ),
    ]
