# Generated by Django 2.2.7 on 2019-11-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0071_faction_simutree'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='respect',
            field=models.IntegerField(default=0),
        ),
    ]
