# Generated by Django 2.2.5 on 2019-11-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0044_auto_20191108_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('heading', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='BannerImage',
        ),
    ]
