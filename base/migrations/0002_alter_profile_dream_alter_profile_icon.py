# Generated by Django 4.0.4 on 2022-04-14 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dream',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='ビジョンボード'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='アイコン'),
        ),
    ]