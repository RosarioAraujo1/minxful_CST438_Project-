# Generated by Django 2.2.7 on 2019-11-25 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minxful_app', '0002_auto_20191121_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='body_text',
            field=models.CharField(default=None, max_length=1000),
            preserve_default=False,
        ),
    ]
