# Generated by Django 4.2.4 on 2023-08-04 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContentApp', '0005_imagen_noticia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagen',
            name='noticia',
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
