# Generated by Django 5.1.6 on 2025-05-06 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Наименование партнера'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name_en',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='Наименование партнера'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name_ru',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='Наименование партнера'),
        ),
    ]
