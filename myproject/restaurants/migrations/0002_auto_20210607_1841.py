# Generated by Django 3.2.4 on 2021-06-07 18:41

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='success',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='profilePic',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='static/images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='profilePic',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='static/images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='coverPic',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='static/images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='profilePic',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='static/images/%Y/%m/%d'),
        ),
    ]
