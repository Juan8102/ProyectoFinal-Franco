# Generated by Django 4.2.4 on 2023-08-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContentApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes')),
            ],
        ),
        migrations.DeleteModel(
            name='Destacado',
        ),
        migrations.AddField(
            model_name='noticia',
            name='cuerpo',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='noticia',
            name='cuerpo_completo',
            field=models.CharField(max_length=24000, null=True),
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='autor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='subtitulo',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]
