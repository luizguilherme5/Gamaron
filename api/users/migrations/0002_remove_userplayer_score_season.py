# Generated by Django 2.1.3 on 2018-11-07 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userplayer',
            name='score_season',
        ),
    ]