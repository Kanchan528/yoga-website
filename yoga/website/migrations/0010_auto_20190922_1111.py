# Generated by Django 2.2.5 on 2019-09-22 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_yogadetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainersDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='describe here')),
            ],
        ),
        migrations.RemoveField(
            model_name='trainers',
            name='description',
        ),
    ]
