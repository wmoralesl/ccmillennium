# Generated by Django 5.2 on 2025-04-12 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_photo_course_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='courses'),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
