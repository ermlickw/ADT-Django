# Generated by Django 2.0.5 on 2018-08-16 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADT', '0004_auto_20180816_1619'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Document',
            new_name='File',
        ),
        migrations.AlterField(
            model_name='claim',
            name='number',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
