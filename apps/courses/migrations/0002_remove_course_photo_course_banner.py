# Generated by Django 5.2 on 2025-04-11 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='photo',
        ),
        migrations.AddField(
            model_name='course',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='courses/'),
        ),
    ]
