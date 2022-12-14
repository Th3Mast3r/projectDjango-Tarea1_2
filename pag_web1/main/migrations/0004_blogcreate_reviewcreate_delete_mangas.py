# Generated by Django 4.1.1 on 2022-09-14 14:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_reviews_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog-create')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Create Blog',
                'verbose_name_plural': 'Create Blog',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='ReviewCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='review-create')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Create Review',
                'verbose_name_plural': 'Create Review',
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Mangas',
        ),
    ]
