# Generated by Django 2.2.5 on 2019-11-06 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20191106_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='website.BlogSingle'),
        ),
    ]
