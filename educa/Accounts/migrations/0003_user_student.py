# Generated by Django 2.2.1 on 2019-06-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_auto_20190623_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Student',
            field=models.BooleanField(default=True),
        ),
    ]