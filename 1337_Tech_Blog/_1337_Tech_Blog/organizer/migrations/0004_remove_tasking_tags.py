# Generated by Django 2.2.6 on 2019-10-25 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0003_auto_20191024_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasking',
            name='tags',
        ),
    ]
