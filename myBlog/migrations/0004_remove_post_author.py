# Generated by Django 4.2.7 on 2023-11-02 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0003_alter_addarticle_new_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]