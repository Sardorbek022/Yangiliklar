# Generated by Django 5.1 on 2024-08-11 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_newsmodel_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsmodel',
            name='view_count',
        ),
    ]
