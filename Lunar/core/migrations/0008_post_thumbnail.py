# Generated by Django 4.1 on 2022-09-24 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_userprofile_avatar_alter_userprofile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
    ]
