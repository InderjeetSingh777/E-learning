# Generated by Django 2.2.1 on 2019-06-23 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]