# Generated by Django 2.2.3 on 2020-03-05 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('glasmarket', '0005_auto_20200305_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='glasmarket.Category'),
            preserve_default=False,
        ),
    ]
