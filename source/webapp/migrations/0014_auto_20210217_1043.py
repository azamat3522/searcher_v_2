# Generated by Django 2.2 on 2021-02-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20210217_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='address',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Адрес и место поставки'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='lots_name',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Наименование лота'),
        ),
    ]
