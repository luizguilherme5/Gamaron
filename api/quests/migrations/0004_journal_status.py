# Generated by Django 2.1.3 on 2018-11-13 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0003_remove_journal_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
