# Generated by Django 3.1.6 on 2021-02-27 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0002_auto_20210227_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=models.TextField(verbose_name='What is on your mind?'),
        ),
    ]
