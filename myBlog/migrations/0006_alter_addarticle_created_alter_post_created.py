# Generated by Django 4.2.7 on 2023-11-02 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0005_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addarticle',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
