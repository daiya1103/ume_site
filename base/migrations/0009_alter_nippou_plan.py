# Generated by Django 4.0.4 on 2022-05-09 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_user_teacher_delete_connection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nippou',
            name='plan',
            field=models.TextField(blank=True, default='', null=True, verbose_name='その他'),
        ),
    ]
