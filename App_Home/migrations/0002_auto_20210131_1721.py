# Generated by Django 3.1.4 on 2021-01-31 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='notice_title',
            field=models.CharField(max_length=5000, verbose_name='Notice Title'),
        ),
    ]
