# Generated by Django 3.1.7 on 2021-05-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210421_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='star',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='stock',
            field=models.IntegerField(),
        ),
    ]