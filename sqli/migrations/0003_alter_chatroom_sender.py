# Generated by Django 4.2.7 on 2023-11-18 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqli', '0002_chatroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='sender',
            field=models.TextField(max_length=1000),
        ),
    ]
