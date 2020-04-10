# Generated by Django 2.2.5 on 2019-09-20 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='describe here')),
            ],
        ),
        migrations.CreateModel(
            name='BlogDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(default='describe here')),
            ],
        ),
        migrations.CreateModel(
            name='ClassesDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='describe here')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('description', models.TextField(default='describe here')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(default='describe here')),
            ],
        ),
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='describe here')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='classes',
            name='description',
        ),
        migrations.AddField(
            model_name='classes',
            name='heading',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
