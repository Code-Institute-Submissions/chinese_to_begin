# Generated by Django 3.0.8 on 2020-08-27 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200802_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='sku',
            field=models.CharField(max_length=20),
        ),
    ]