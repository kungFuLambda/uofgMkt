# Generated by Django 2.2.3 on 2020-03-05 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasmarket', '0006_listing_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='picture',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]