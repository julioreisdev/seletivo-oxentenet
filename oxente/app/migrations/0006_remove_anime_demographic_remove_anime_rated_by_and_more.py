# Generated by Django 4.0.5 on 2022-06-14 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_anime_eps_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='demographic',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='rated_by',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='source',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='status',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='theme',
        ),
    ]
