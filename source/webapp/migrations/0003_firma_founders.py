# Generated by Django 2.2 on 2021-02-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_firma_founders'),
    ]

    operations = [
        migrations.AddField(
            model_name='firma',
            name='founders',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Учредители'),
        ),
    ]
