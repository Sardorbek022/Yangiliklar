# Generated by Django 5.0.6 on 2024-06-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_newsmodel_publish_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='slug',
            field=models.SlugField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='status',
            field=models.CharField(choices=[('Faol emas', 'Faol emas'), ('Faol', 'Faol')], default='Faol emas', max_length=50, verbose_name='Holati'),
        ),
    ]
