# Generated by Django 3.2.4 on 2021-06-03 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20210603_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='picture',
            new_name='coverPic',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='picture',
            new_name='coverPic',
        ),
        migrations.AddField(
            model_name='company',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]