# Generated by Django 2.2.7 on 2019-11-25 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minxful_app', '0004_auto_20191125_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='minxful_app.Post'),
        ),
    ]
