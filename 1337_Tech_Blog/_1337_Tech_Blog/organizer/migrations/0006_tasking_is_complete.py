# Generated by Django 2.2.6 on 2019-11-06 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0005_tasking_project_codename'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasking',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
