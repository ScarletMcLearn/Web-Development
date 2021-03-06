# Generated by Django 3.1.5 on 2021-01-09 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('published_date', models.DateField(auto_now_add=True, verbose_name='Date Published')),
                ('edited_date', models.DateField(auto_now_add=True, verbose_name='Date Edited')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('commented_date', models.DateField(auto_now_add=True, verbose_name='Date Published')),
                ('edited_date', models.DateField(auto_now_add=True, verbose_name='Date Edited')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]
