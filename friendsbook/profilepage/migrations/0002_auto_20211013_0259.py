# Generated by Django 3.2.6 on 2021-10-13 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepage',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='profilepage',
            name='object_id',
        ),
    ]
