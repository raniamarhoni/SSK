# Generated by Django 3.1.7 on 2021-04-21 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210413_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='size',
            name='sku',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
