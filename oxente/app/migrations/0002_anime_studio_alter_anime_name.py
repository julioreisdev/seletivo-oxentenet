# Generated by Django 4.0.5 on 2022-06-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='studio',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='anime',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]