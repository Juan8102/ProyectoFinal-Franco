# Generated by Django 4.2.4 on 2023-08-04 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContentApp', '0006_remove_imagen_noticia_noticia_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='cuerpo_completo',
        ),
        migrations.AlterField(
            model_name='noticia',
            name='cuerpo',
            field=models.CharField(max_length=24000, null=True),
        ),
    ]