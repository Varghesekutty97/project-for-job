# Generated by Django 3.2.7 on 2021-09-23 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210923_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user_id',
        ),
    ]
