# Generated by Django 2.2.1 on 2019-06-26 11:11

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20190626_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=courses.models.content_file_name),
        ),
    ]
