# Generated by Django 2.0.5 on 2018-08-16 23:40

import ADT.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADT', '0005_auto_20180816_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='uploaded_at',
        ),
        migrations.AlterField(
            model_name='file',
            name='document',
            field=models.FileField(upload_to=ADT.models.File.only_filename),
        ),
    ]
