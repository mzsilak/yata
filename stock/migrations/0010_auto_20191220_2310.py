# Generated by Django 2.2.7 on 2019-12-20 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_auto_20190728_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='priceHistory',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='quantityHistory',
        ),
    ]
