# Generated by Django 5.2 on 2025-04-29 23:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_heading', models.CharField(max_length=255, unique=True)),
                ('project_description_1', models.TextField()),
                ('project_description_2', models.TextField()),
                ('primary_image', models.ImageField(upload_to='project_images/')),
                ('project_video', models.FileField(blank=True, null=True, upload_to='project_videos/')),
                ('project_url', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.project')),
            ],
        ),
    ]
