# Generated by Django 2.2.5 on 2019-09-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20190922_0739'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.AddField(
            model_name='moredetails',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
