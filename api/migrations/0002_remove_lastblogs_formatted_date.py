# Generated by Django 5.0.6 on 2024-06-28 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastblogs',
            name='formatted_date',
        ),
    ]
