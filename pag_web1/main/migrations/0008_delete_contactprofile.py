# Generated by Django 4.1.1 on 2022-09-14 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_blogs_options_alter_contactprofile_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactProfile',
        ),
    ]
