# Generated by Django 2.0.5 on 2018-08-20 21:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ADT', '0012_delete_nothing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claim',
            name='para',
        ),
        migrations.AddField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]