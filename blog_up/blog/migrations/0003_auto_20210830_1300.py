# Generated by Django 3.2.5 on 2021-08-30 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210708_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=987),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.TextField(max_length=987, unique=True),
        ),
    ]