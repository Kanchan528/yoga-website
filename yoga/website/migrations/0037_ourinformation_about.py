# Generated by Django 2.2.5 on 2019-11-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_auto_20191106_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourinformation',
            name='about',
            field=models.TextField(default='describe here'),
        ),
    ]