# Generated by Django 4.1.1 on 2024-04-18 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_mymod_email_alter_mymod_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymod',
            name='batch',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mymod',
            name='qulification',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
