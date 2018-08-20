# Generated by Django 2.0.5 on 2018-08-20 18:25

import ADT.models
import ADT.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADT', '0010_remove_file_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='appNumber',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='file',
            name='document',
            field=models.FileField(blank=True, upload_to=ADT.models.File.only_filename, validators=[ADT.validators.validate_file_extension]),
        ),
    ]