# Generated by Django 5.0.6 on 2024-06-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_lastblogs_formatted_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lastblogs',
            old_name='formatted_date',
            new_name='chislo',
        ),
        migrations.AddField(
            model_name='lastblogs',
            name='oy',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
