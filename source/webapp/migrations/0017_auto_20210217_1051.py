# Generated by Django 2.2 on 2021-02-17 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_auto_20210217_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='product',
            name='okgz',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Класс ОКГЗ'),
        ),
    ]
