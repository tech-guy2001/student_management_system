# Generated by Django 4.1.1 on 2024-04-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_mymod_delete_mymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymod',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='mymod',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]
