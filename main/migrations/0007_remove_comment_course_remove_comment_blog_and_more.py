# Generated by Django 5.0.1 on 2024-07-25 23:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_comment_blog_comment_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.blog'),
            preserve_default=False,
        ),
    ]