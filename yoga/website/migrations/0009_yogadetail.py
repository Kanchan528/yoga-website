# Generated by Django 2.2.5 on 2019-09-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20190922_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='YogaDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('heading', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(default='describe here')),
            ],
        ),
    ]
