# Generated by Django 5.0.7 on 2024-07-15 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(default='/', max_length=255),
        ),
    ]
