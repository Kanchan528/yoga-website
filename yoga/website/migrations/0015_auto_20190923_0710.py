# Generated by Django 2.2.5 on 2019-09-23 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20190923_0657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yogatype1',
            old_name='time',
            new_name='date',
        ),
    ]