# Generated by Django 5.0.2 on 2024-05-06 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='post_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='notification',
            name='post_type',
            field=models.CharField(default='stage', max_length=20),
        ),
    ]
