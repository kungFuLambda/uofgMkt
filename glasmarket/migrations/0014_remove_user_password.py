# Generated by Django 2.2.3 on 2020-03-06 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glasmarket', '0013_auto_20200306_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]