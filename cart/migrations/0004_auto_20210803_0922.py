# Generated by Django 2.2 on 2021-08-03 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20210802_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='active',
        ),
        migrations.RemoveField(
            model_name='items',
            name='quan',
        ),
    ]
