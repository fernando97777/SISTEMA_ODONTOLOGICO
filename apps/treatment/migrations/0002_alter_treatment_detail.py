# Generated by Django 4.1.4 on 2022-12-09 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='detail',
            field=models.CharField(max_length=100, verbose_name='Tipo de tratamiento'),
        ),
    ]
