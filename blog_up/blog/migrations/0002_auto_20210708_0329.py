# Generated by Django 3.2.5 on 2021-07-08 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.TextField(unique=True),
        ),
    ]
