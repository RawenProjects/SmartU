# Generated by Django 5.0.3 on 2024-04-28 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_evenement_interesses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='est_reserve',
        ),
    ]