# Generated by Django 3.0.5 on 2020-06-11 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200610_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='elo',
            name='k_factor',
            field=models.IntegerField(default=32),
        ),
        migrations.AlterField(
            model_name='elo',
            name='rating',
            field=models.IntegerField(default=1200),
        ),
    ]