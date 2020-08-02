# Generated by Django 3.0.8 on 2020-08-01 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200726_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='before_discount',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Category'),
        ),
    ]