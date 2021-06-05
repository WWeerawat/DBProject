# Generated by Django 3.2.3 on 2021-06-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_member_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(choices=[('AD', 'admin'), ('EX', 'executive'), ('MA', 'manager'), ('ST', 'staff'), ('ME', 'member')], default='ME', max_length=3),
        ),
    ]
