# Generated by Django 3.2.4 on 2021-06-07 05:55

from django.db import migrations, models
import django.utils.timezone
import queueSystem.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('queueID', models.CharField(default=queueSystem.models.Queue.genID, max_length=10, primary_key=True, serialize=False)),
                ('peopleNum', models.IntegerField(default=0)),
                ('queueCreated', models.DateTimeField(auto_now_add=True)),
                ('reserveDateTime', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('status', models.CharField(choices=[('success', 'success'), ('fail', 'fail'), ('waiting', 'waiting'), ('cancel', 'cancel'), ('point', 'point')], default='waiting', max_length=10)),
                ('queueIsPass', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Queue',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewID', models.CharField(default=queueSystem.models.Review.genID, max_length=10, primary_key=True, serialize=False)),
                ('detail', models.CharField(max_length=200)),
                ('rating', models.FloatField(default=0)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Review',
            },
        ),
    ]
