# Generated by Django 2.2.5 on 2019-11-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_auto_20191106_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='describe here')),
            ],
        ),
        migrations.DeleteModel(
            name='ClassesDescription',
        ),
    ]
