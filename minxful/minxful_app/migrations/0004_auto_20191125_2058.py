# Generated by Django 2.2.7 on 2019-11-25 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minxful_app', '0003_reply_body_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='body_text',
            field=models.CharField(default='', max_length=1000),
        ),
    ]