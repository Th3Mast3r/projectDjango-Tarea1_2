# Generated by Django 4.1.1 on 2022-09-14 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_blogcreate_reviewcreate_delete_mangas'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogCreate',
        ),
        migrations.DeleteModel(
            name='ReviewCreate',
        ),
        migrations.AlterModelOptions(
            name='blogs',
            options={'ordering': ['author'], 'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='timestamp',
        ),
    ]
