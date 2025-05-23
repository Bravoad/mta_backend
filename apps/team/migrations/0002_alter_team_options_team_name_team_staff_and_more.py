# Generated by Django 5.1.6 on 2025-05-06 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['order'], 'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Имя сотрудника'),
        ),
        migrations.AddField(
            model_name='team',
            name='staff',
            field=models.CharField(default='', max_length=255, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='team',
            name='is_displayed',
            field=models.BooleanField(default=True, verbose_name='Показать'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name_en',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='Имя сотрудника'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name_ru',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='Имя сотрудника'),
        ),
        migrations.AlterField(
            model_name='team',
            name='staff_en',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='team',
            name='staff_ru',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='Должность'),
        ),
    ]
