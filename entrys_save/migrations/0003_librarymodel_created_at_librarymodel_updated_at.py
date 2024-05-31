# Generated by Django 5.0.4 on 2024-05-26 04:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrys_save', '0002_tagsmodel_entrymodel_likes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarymodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='librarymodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
