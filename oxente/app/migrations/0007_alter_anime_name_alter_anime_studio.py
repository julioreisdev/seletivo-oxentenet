# Generated by Django 4.0.5 on 2022-06-14 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_anime_demographic_remove_anime_rated_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='anime',
            name='studio',
            field=models.CharField(max_length=255),
        ),
    ]
