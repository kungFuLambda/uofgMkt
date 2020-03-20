# Generated by Django 2.2.3 on 2020-03-10 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasmarket', '0020_listing_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(blank=True, help_text='Facebook'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=128),
        ),
    ]