# Generated by Django 2.2 on 2021-02-12 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20210211_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openbudget',
            name='payer',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Плательщик'),
        ),
    ]
