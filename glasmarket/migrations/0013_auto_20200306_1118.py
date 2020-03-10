# Generated by Django 2.2.3 on 2020-03-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasmarket', '0012_auto_20200305_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=' ', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]