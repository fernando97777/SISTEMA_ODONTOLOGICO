# Generated by Django 4.1.4 on 2022-12-10 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='image',
            field=models.ImageField(null=True, upload_to='proyectos', verbose_name='Imagen'),
        ),
    ]