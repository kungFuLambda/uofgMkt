# Generated by Django 2.2.3 on 2020-03-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasmarket', '0017_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]