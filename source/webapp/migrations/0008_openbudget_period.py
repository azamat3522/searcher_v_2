# Generated by Django 2.2 on 2021-02-11 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_remove_openbudget_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='openbudget',
            name='period',
            field=models.CharField(blank=True, max_length=220, null=True, verbose_name='Период'),
        ),
    ]
