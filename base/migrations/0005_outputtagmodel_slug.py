# Generated by Django 4.0.4 on 2022-04-22 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_outputtagmodel_output_output_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='outputtagmodel',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='URL'),
        ),
    ]
