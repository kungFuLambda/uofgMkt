# Generated by Django 2.2.3 on 2020-03-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasmarket', '0021_auto_20200310_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
