# Generated by Django 2.2 on 2021-02-11 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_openbudget_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openbudget',
            name='purpose_of_payment',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Назначение платежа'),
        ),
    ]
