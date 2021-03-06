# Generated by Django 2.2.6 on 2019-10-21 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32)),
                ('slug', models.SlugField(max_length=32)),
                ('asignee', models.CharField(db_index=True, max_length=16)),
                ('description', models.TextField()),
                ('assigned_date', models.DateTimeField(auto_now_add=True, verbose_name='date assigned')),
                ('tags', models.ManyToManyField(to='organizer.Tag')),
            ],
            options={
                'ordering': ['name'],
                'get_latest_by': 'assigned_date',
            },
        ),
    ]
