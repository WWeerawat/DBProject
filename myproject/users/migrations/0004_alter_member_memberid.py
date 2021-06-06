# Generated by Django 3.2.4 on 2021-06-07 06:03

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_member_memberid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='memberID',
            field=models.CharField(default=users.models.Member.genID, max_length=50, primary_key=True, serialize=False),
        ),
    ]