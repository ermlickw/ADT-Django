# Generated by Django 2.0.5 on 2018-08-20 23:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ADT', '0013_auto_20180820_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='claim',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
