# Generated by Django 3.2.6 on 2021-10-22 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0004_useraccount_favorite_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='profile_photos'),
        ),
    ]
