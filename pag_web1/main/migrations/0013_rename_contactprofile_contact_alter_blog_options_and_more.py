# Generated by Django 4.1.1 on 2022-09-16 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_blog_contactprofile_delete_blogs_delete_contact_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactProfile',
            new_name='Contact',
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['timestamp'], 'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['timestamp'], 'verbose_name': 'Contact', 'verbose_name_plural': 'Contact'},
        ),
    ]
