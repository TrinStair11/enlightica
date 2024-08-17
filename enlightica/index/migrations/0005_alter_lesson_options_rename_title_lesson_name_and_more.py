# Generated by Django 5.1 on 2024-08-17 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_remove_courseaccess_user_remove_payment_user_lesson_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={},
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='video_url',
        ),
        migrations.AddField(
            model_name='course',
            name='related_courses',
            field=models.ManyToManyField(blank=True, to='index.course'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=models.FileField(blank=True, upload_to='static/lesson_videos/'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.course'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='order',
            field=models.IntegerField(),
        ),
    ]
