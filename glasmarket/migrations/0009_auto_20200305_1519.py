# Generated by Django 2.2.3 on 2020-03-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasmarket', '0008_auto_20200305_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default="{% static 'images/stock.jpg' %}", upload_to=''),
        ),
    ]