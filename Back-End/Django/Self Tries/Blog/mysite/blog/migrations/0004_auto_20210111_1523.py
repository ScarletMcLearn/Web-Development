# Generated by Django 3.1.5 on 2021-01-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210110_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edited_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Edited'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Published'),
        ),
    ]