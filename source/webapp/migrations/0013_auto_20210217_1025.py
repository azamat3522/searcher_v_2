# Generated by Django 2.2 on 2021-02-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_auto_20210217_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='org_name',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Название организации'),
        ),
    ]
