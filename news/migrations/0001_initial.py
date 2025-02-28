# Generated by Django 5.0.6 on 2024-06-30 11:09

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Kategoriya nomi')),
            ],
            options={
                'verbose_name': 'Kategoriyalar',
                'verbose_name_plural': 'Kategoriyalar',
                'db_table': 'Categorys',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ism')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Xabar')),
            ],
            options={
                'verbose_name': 'Aloqa',
                'verbose_name_plural': 'Aloqa',
                'db_table': 'Contact',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Yangilik nomi')),
                ('slug', models.SlugField(max_length=250)),
                ('body', models.TextField(verbose_name="Yangilik haqida ma'lumotlar")),
                ('image', models.ImageField(upload_to='news/images', verbose_name='Rasmi')),
                ('publish_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updeted_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Faol emas', 'Deactive'), ('Faol', 'Active')], default='Faol emas', max_length=50, verbose_name='Holati')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.categorymodel', verbose_name='Kategoriyasi')),
            ],
            options={
                'verbose_name': 'Yangiliklar',
                'verbose_name_plural': 'Yangiliklar',
                'db_table': 'News',
                'ordering': ['-publish_time'],
                'managed': True,
            },
        ),
    ]
