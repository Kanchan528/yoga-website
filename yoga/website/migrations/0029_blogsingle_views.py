# Generated by Django 2.2.5 on 2019-11-06 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0028_postcomment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogsingle',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
