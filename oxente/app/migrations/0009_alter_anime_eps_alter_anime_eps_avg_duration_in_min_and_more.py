# Generated by Django 4.0.5 on 2022-06-14 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_anime_demographic_anime_eps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='eps',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='anime',
            name='eps_avg_duration_in_min',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='anime',
            name='rating',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='anime',
            name='year',
            field=models.CharField(default='', max_length=255),
        ),
    ]
