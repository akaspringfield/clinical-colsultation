# Generated by Django 3.0.3 on 2020-05-21 14:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
