# Generated by Django 2.2 on 2021-02-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_tender_count_of_lots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='purchases_name',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Наименование закупки'),
        ),
    ]
